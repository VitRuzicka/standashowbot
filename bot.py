import socket, string
import standa_hlasky

# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "yournickname"
PORT = 6667
PASS = "your o:auth token"
readbuffer = ""
MODT = False

# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #standashow \r\n")

# Function for seding messages
def Send_message_priv(message):
    s.send("PRIVMSG #standashow :" + message + "\r\n")

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        # Checks whether the message is PING because its a method of Twitch to check if you're afk
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            # Splits the given string so we can work with it better
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    # Sets the message variable to the actual message sent
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""
                # Sets the username variable to the actual username
                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
                
                # Only works after twitch is done announcing stuff (MODT = Message of the day)
                if MODT:
                    print (username + ": " + message)
                    
                    # You can add all your plain commands here
                    if "ahoj" in message.lower():
                        Send_message_priv("Ahoj, " + username)
                    elif message.startswith('!'):
                        if "citat" in message.lower():
                            Send_message_priv(standa_hlasky.hlaska(standa_hlasky.cislo(message)))


                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True
