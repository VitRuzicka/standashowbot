# -*- coding: utf-8 -*-
import socket, string
import standa_hlasky2
import random
# Set all the variables necessary to connect to Twitch IRC
HOST = "irc.twitch.tv"
NICK = "ch4tb0t"
PORT = 6667
PASS = "oauth:y3fq3o7f3t78f2xwnnw7468g1rz7w8"
cteniBuf = ""
ready = False
pozdravy = ["ahoj!", "zdravím", "zdravíčko", "ahojky", "zdarec", "rád tě vidím", "nazdárek"]
# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #standashow \r\n")

# a function for sending message
def Send_message_priv(message):
    s.send("PRIVMSG #standashow :" + message + "\r\n")

while True:
    cteniBuf = cteniBuf + s.recv(1024)
    cast = string.split(cteniBuf, "\n")
    cteniBuf = cast.pop()

    for radek in cast:
        # responds to twitch's PING - PONG to let twitch know we know
        if (radek[0] == "PING"):
            s.send("PONG %s\r\n" % radek[1])
        else:
            # splits string to name and message
            casti = string.split(radek, ":")

            if "QUIT" not in casti[1] and "JOIN" not in casti[1] and "PART" not in casti[1]:
                try:
                    # sets message var to actual message
                    message = casti[2][:len(casti[2]) - 1]
                except:
                    message = ""
                # sets username to actual username
                usernamesplit = string.split(casti[1], "!")
                username = usernamesplit[0]
                
                # starts only when twitch is ready
                if ready:
                    print (username + ": " + message)
                    
                    # prikazy pro ruzne aktivity
                    if "ahoj" in message.lower():
                        Send_message_priv("@" + username +  " " + pozdravy[random.randint(0, len(pozdravy)-1)])
                    elif message.startswith('!'):
                        if "citat" in message.lower():
                            Send_message_priv(standa_hlasky2.hlaska(standa_hlasky2.cislo(message)))


                for y in casti:
                    if "End of /NAMES list" in y:
                        ready = True
