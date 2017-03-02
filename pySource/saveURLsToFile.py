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
    soup = BeautifulSoup(fetchClass.responseHTML, "html.parser")
    names = soup.find_all('a', attrs={'href' : re.compile("^/pros/(?!new)")})
    for name in names:
        if name:
            fetchResults.append(homePage.home_page + name.get('href'))
            
with open('links.py', 'a') as file:
    for item in fetchResults:
        file.write("%s\n" % item)