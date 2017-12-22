#http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

with open("ark.txt", "r") as f:
     lines = f.readlines()
     lines = [x.strip() for x in lines]

s = open("subjects.txt", "a")

for line in lines:
     page = requests.get(line)
     tree = html.fromstring(page.content)
     #This will hopefully create a list of buyers:
     subjects = tree.xpath('//a[contains(@href,"subjects")]/text()')
     title = tree.xpath('//title/text()')
     s.write(str(title)+'   '+str(subjects)+'\n')

s.close()
f.close()
