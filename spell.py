from urllib.request import urlopen
import config
from bs4 import BeautifulSoup

class Spell:
    def __init__(self, slug):
        self.parseurl = config.App.sUrlBase + config.App.sUrlSpell + slug
        self.level = 1
        self.name = 'a'
        self.slug = slug
        self.description = ''
        self.castTime = ''
        self.duration = ''
        self.school = ''
        self.compo = ''
        self.ritual = False
        self.range = ''
        self.source = ''

    def parseSpell(self):
        pass

