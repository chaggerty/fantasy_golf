from lxml import html
import sys
import requests
import string

for arg in sys.argv[1:]:
    if arg == '-h':
        print 'best_players_available.py -i string-of-tourny-name'
        sys.exit()
    elif arg in ("-i","--ifile"):
	inp = sys.argv[2]
page = requests.get('http://www.pgatour.com/stats/stat.186.html') #player rankings
tree = html.fromstring(page.text)
players = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page1 = requests.get('http://www.pgatour.com/stats/stat.02671.html') #current FedEx Cup rankings
tree = html.fromstring(page1.text)
fedex = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page2 = requests.get('http://www.pgatour.com/tournaments/'+ inp +'/field.html') 
tree2 = html.fromstring(page2.content)
field = tree2.xpath('//div[@class="field-table-content clearfix"]/div/p/text()')

lineup = []
print("Based on world rankings:")
for guy in players:
	temp = string.split(guy)
	last_name = temp[1]
	first_name = temp[0]
	for f in field:
		if last_name in f and first_name in f: 
			lineup.append(f)
			if len(lineup) ==7:
				print(lineup)
			break	
			 
print("Based on FedEx Cup Rankings:")
lineup = []
for guy in fedex:
	temp = string.split(guy)
	last_name = temp[1]
	first_name = temp[0]
	for f in field:
		if last_name in f and first_name in f: 
			lineup.append(f)
			if len(lineup) ==7:
				print(lineup)
			break
