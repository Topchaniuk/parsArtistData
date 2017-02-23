import fetchURL
#import parseHTML
from bs4 import BeautifulSoup
import sys
import re

fetchResults = []
equipment = []
pile = []
links = []


with open("links.py", "r") as f:
    linksDr = f.read()

for line in linksDr:
    links = linksDr.split("\n")

print links

