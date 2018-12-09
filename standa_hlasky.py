# -*- coding: utf-8 -*-
#!/usr/bin/python3
import urllib3
url ='https://twitch.center/customapi/quote/list?token=80580068'

def hlaska(x):
	http_pool = urllib3.connection_from_url(url)
	r = http_pool.urlopen('GET',url)
	hlasky = r.data.decode('utf-8').split('\n')
	if int(x) < (len(hlasky) - 1):
		return hlasky[int(x) - 1]
	else:
		return "neplatne cislo"

def cislo(retezec):
	for znak in retezec.split():
		if znak.isdigit():
			return znak
