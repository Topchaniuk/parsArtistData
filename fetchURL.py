import urllib2

class FetchURL:
    def __init__(self):
        self.responseHTML = ''
    def fetch(self, urlToOpen):
        response = urllib2.urlopen(urlToOpen)
        self.responseHTML = response.read()