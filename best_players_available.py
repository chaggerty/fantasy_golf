#!/usr/local/bin/python

from lxml import html
import sys
import requests
import string
import json

page = requests.get('http://www.pgatour.com/stats/stat.186.html') #player rankings
tree = html.fromstring(page.text)
players = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page1 = requests.get('http://www.pgatour.com/stats/stat.02671.html') #current FedEx Cup rankings
tree = html.fromstring(page1.text)
fedex = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page2 = requests.get('http://www.pgatour.com/data/r/'+ sys.argv[1] +'/field.json')
tree2 = page2.json()
field = tree2['Tournament']['Players']


lineup = []
print("Based on world rankings:")
for guy in players:
	temp = string.split(guy)
	last_name = temp[1]
	first_name = temp[0]
	for f in field:
		if last_name in f['PlayerName'] and first_name in f['PlayerName']: 
			lineup.append(str(f['PlayerName']))
			if len(lineup) ==7:
				print(lineup)
			break	
			 
print("\nBased on FedEx Cup Rankings:")
lineup = []
for guy in fedex:
	temp = string.split(guy)
	last_name = temp[1]
	first_name = temp[0]
	for f in field:
		if last_name in f['PlayerName'] and first_name in f['PlayerName']: 
			lineup.append(str(f['PlayerName']))
			if len(lineup) ==7:
				print(lineup)
			break
