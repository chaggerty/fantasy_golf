from lxml import html
import requests
import string
page = requests.get('http://www.pgatour.com/stats/stat.186.html') #player rankings
tree = html.fromstring(page.text)
players = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page2 = requests.get('http://www.pgatour.com/tournaments/sony-open-in-hawaii/field.html') #update with current tournament
tree2 = html.fromstring(page2.content)
field = tree2.xpath('//div[@class="field-table-content clearfix"]/div/p/text()')

lineup = []

for guy in players:
	temp = string.split(guy)
	guys_last_name = temp[1]
	for f in field:
		if guys_last_name in f:
			lineup.append(f)
			if len(lineup) ==7:
				print(lineup)
				continue
			 
	
#next: add ranking of each player to the lineup as a check
