import fetchURL
from bs4 import BeautifulSoup
import sys
import re
import homePage
import targetLinks

fetchResults = []
fetchClass = fetchURL.FetchURL()

for link in targetLinks.target_links.itervalues():
    fetchClass.fetch(homePage.home_page + link)
#print fetchClass.responseHTML
#print sys.stdout.encoding


    soup = BeautifulSoup(fetchClass.responseHTML, "html.parser")
#parser = parseHTML.MyHTMLParser()
#parser.feed(fetchClass.responseHTML)
    names = soup.find_all('a', attrs={'href' : re.compile("^/pros/(?!new)")})
    for name in names:
        if name:
            fetchResults.append(homePage.home_page + name.get('href'))
#print name.get('href')
#.text.encode('utf-8')
#print fetchResults
#print names
with open('links.py', 'a') as file:
    for item in fetchResults:
        file.write("%s\n" % item)