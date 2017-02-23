
fetchClass = fetchURL.FetchURL()



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