from urllib.request import urlopen
import config 
from bs4 import BeautifulSoup
from spell import Spell

class SpellList:
    list = set()
    def __init__(self, id):
        self.parseurl = config.App.sUrlBase + config.App.sUrlSpellBooks + id

    def parseList(self):
        content = urlopen(self.parseurl).read().decode()
        soup = BeautifulSoup(content, 'html.parser')
        spells = soup.find_all('input',attrs={'name':'select_sorts[]'})
        for s in spells:
            print(s.parent.text)
            #self.list.add(Spell(''))
