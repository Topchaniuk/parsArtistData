import urllib2
#import requests

class FetchURL:
    def __init__(self):
        self.responseHTML = ''
    def fetch(self, urlToOpen):
        response = urllib2.urlopen(urlToOpen)
        #response = requests.get(urlToOpen)
        self.responseHTML = response.read()
        #self.responseHTML = response.text