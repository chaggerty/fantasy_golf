from lxml import html
import requests
page = requests.get('http://www.pgatour.com/stats/stat.186.html') #player rankings
tree = html.fromstring(page.text)
players = tree.xpath('//*[contains(@id, "playerStatsRow")]/td[3]/a/text()')
page2 = requests.get('http://www.pgatour.com/tournaments/sony-open-in-hawaii/field.html') #update with current tournament
tree2 = html.fromstring(page2.content)
field = tree2.xpath('//div[@class="field-table-content clearfix"]/div/p/text()')

top_players = players[0:99] #top 100

#now need to figure out how to determine intersection of these lists, which is non-trivial since the name formatting is different


