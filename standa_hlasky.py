# -*- coding: utf-8 -*-
#!/usr/bin/python3
import urllib2
url = "https://twitch.center/customapi/quote/list?token=80580068"

def hlaska(cislo):
	response = urllib2.urlopen(url)
	data = response.read()
	citat = data.split('\n')
	#print citat[76] #cislo v zavorce urcuje kolikaty citat v poradi je vypsan 
	if cislo > len(citat) - 1:
		return citat[int(cislo) - 1]
	else:
		return "neplatne_cislo"


def cislo(retezec):
	for znak in retezec.split():
		if znak.isdigit():
			return znak
