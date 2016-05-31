from bs4 import BeautifulSoup
from urllib.request import urlopen
from charClass import CharClass
from spellList import SpellList

class App:
    sUrlBase = "http://www.aidedd.org/"
    sUrlSpellBooks = "adj/livre-sorts/?n=19&c="
    sUrlSpell = "dnd/sorts.php?vf="
    setClasses = set()

    def run(self):
        sHtmlContent = urlopen(self.sUrlBase + self.sUrlSpellBooks + 'c').read().decode()
        soup = BeautifulSoup(sHtmlContent,'html.parser')
        setOptions = soup.find(id='Form_Form_classe').find_all('option')

        for o in setOptions:
            self.setClasses.add(CharClass(o['value'], o.text))

        for classe in self.setClasses:
            classe.spellList.parseList()

