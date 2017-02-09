import fetchURL
#import parseHTML
from bs4 import BeautifulSoup
import sys
import re

resourse = 'http://equipboard.com'
fetchResults = []
equipment = []
pile = []

fetchClass1 = fetchURL.FetchURL()
fetchClass2 = fetchURL.FetchURL()
#/role/guitarists
#/role/bassists
#/role/drummers
fetchClass1.fetch(resourse + '/role/bassists')
#print fetchClass.responseHTML
#print sys.stdout.encoding


soup1 = BeautifulSoup(fetchClass1.responseHTML, "html.parser")
#parser = parseHTML.MyHTMLParser()
#parser.feed(fetchClass.responseHTML)
names = soup1.find_all('a', attrs={'href' : re.compile("^/pros/(?!new)")})
for name in names:
    if name:
        fetchResults.append(resourse + name.get('href'))
        #print name.get('href')
        #.text.encode('utf-8')
#print fetchResults
#print names


for result in fetchResults:
    if result:
        fetchClass2.fetch(result)
        pile.append(fetchClass2.responseHTML)

#print fetchClass2.responseHTML

soup2 = BeautifulSoup(pile, "html.parser")



equips = soup2.find_all('h3')
for equip in equips:
    if equip:
        equipment.extend(equip)

print equipment