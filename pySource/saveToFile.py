import fetchURL
from bs4 import BeautifulSoup

class SaveToFile:
    def __init__(self):
        self.fetchResults = []

    def saveToFile(self, links, tagToFetch, filter, fileName):
        fetchClass = fetchURL.FetchURL()
        for link in links:
            print "Processing link: " + link
            fetchClass.fetch(link)

            soup = BeautifulSoup(fetchClass.responseHTML, "html.parser")

            items = soup.find_all(tagToFetch, **filter)
            for item in items:
                if item:
                    self.fetchResults.append(item.text.encode('utf-8'))

        with open(fileName, 'a') as file:
            for item in self.fetchResults:
                file.write("%s\n" % item)