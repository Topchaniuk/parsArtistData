import fetchURL
#import parseHTML
from bs4 import BeautifulSoup
import sys


fetchClass = fetchURL.FetchURL()
#http://equipboard.com/role/guitarists
#http://equipboard.com/role/bassists
fetchClass.fetch('http://equipboard.com/role/drummers')
#print fetchClass.responseHTML
#print sys.stdout.encoding


soup = BeautifulSoup(fetchClass.responseHTML, "html.parser")
#parser = parseHTML.MyHTMLParser()
#parser.feed(fetchClass.responseHTML)
names = soup.find_all('h2')
for name in names:
    if name:
        print name.text.encode('utf-8')

