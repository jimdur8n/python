#http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests


page = requests.get("http://archiveswest.orbiscascade.org/ark:/80444/xv22924/")
tree = html.fromstring(page.content)

#This will hopefully create a list of buyers:
subjects = tree.xpath('//a[contains(@href,"subjects")]/text()')

print('subjects: ',subjects)
