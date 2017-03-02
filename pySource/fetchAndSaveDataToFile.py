import saveToFile
import re

links = []

with open("links.py", "r") as f:
    linksDr = f.read()

links = linksDr.split("\n")
links.pop()

saver = saveToFile.SaveToFile()
filter = {'itemprop' : 'owns'}
saver.saveToFile(links, 'h3', filter, 'rigs.py')