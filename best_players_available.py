from lxml import html
import requests
import string
page = requests.get('http://www.pgatour.com/stats/stat.186.html') #player rankings
tree = html.fromstring(page.text)
players = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page1 = requests.get('http://www.pgatour.com/stats/stat.02671.html') #current FedEx Cup rankings
tree = html.fromstring(page1.text)
fedex = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page2 = requests.get('http://www.pgatour.com/tournaments/careerbuilder-challenge-in-partnership-with-the-clinton-foundation/field.html') #update with current tournament
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
