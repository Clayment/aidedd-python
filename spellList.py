from urllib.request import urlopen
import config 
from bs4 import BeautifulSoup
from spell import Spell
import re
import os
import sys

class SpellList:
    def __init__(self, id, path):
        self.parseurl = config.App.sUrlBase + config.App.sUrlSpellBooks + id
        self.list = set()

        self.sPath = path

        if not os.path.exists(path):
            os.makedirs(path)

    def parseList(self):
        content = urlopen(self.parseurl).read().decode()
        soup = BeautifulSoup(content, 'html.parser')
        spells = soup.find_all('input',attrs={'name':'select_sorts[]'})
        for s in spells:
            matches = re.match('^(\d+)-(.+)$', s.parent.text.strip())
            if matches:
                lvl = matches.group(1)
                name = matches.group(2).strip()
                slug = s['value'].strip().replace('\'', '')
                spell = Spell(slug, lvl, self.sPath)
                self.list.add(spell)
        
        for spell in self.list:
            try:
                spell.parseSpell()
            except:
                print('parseSpell Error: the spell '+ spell.slug +' parsing raised an Error : ', sys.exc_info()[0])


        #for spell in self.list:
        #    print(spell)
