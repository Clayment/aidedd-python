from urllib.request import urlopen
import config
from bs4 import BeautifulSoup
import re


class Spell:
    def __init__(self, slug, level, path):
        self.parseurl = config.App.sUrlBase + config.App.sUrlSpell + slug
        self.html = None;
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
        content = urlopen(self.parseurl).read().decode()
        self.html = BeautifulSoup(content, 'html.parser')
        self.sPath = path

    def parseSpell(self):

        nameelem = self.html.find('div', class_="nom")
        if not nameelem:
            raise ImportError('div.nom not found for ' + self.slug)
        self.name = nameelem.text.strip()

        lvlelem = self.html.find('div', class_="niveau")
        if not lvlelem:
            raise ImportError('div.niveau not found for ' + self.slug)
        lvltext = lvlelem.text.strip()
        matches = re.match('^niveau (\d+) - (\w+)( \(rituel\))?$',lvltext)
        self.level = matches.group(1).strip()
        self.school = matches.group(2).strip()
        self.ritual = True if matches.group(3).strip() else False

        castelem = lvlelem.next_sibling
        casttext = castelem.text.strip()
        matches = re.match('^Temps d\'incantation : (.*)$',casttext)
        self.castTime = matches.group(1).strip()

        rangeelem = castelem.next_sibling
        rangetext = rangeelem.text.strip()
        matches = re.match('^Portée : (.*)$',rangetext)
        self.range = matches.group(1).strip()

        compoelem = rangeelem.next_sibling
        compotext = compoelem.text.strip()
        matches = re.match('^Composantes : (.*)$',compotext)
        self.compo = matches.group(1).strip()

        durationelem = compoelem.next_sibling
        durationtext = durationelem.text.strip()
        matches = re.match('^Durée : (.*)$',durationtext)
        self.duration = matches.group(1).strip()

        descelem = self.html.find('div', class_="description")
        if not descelem:
            raise ImportError('div.description not found for ' + self.slug)
        self.description = descelem.text.strip()

        sourceelem = self.html.find('div', class_="source")
        if not sourceelem:
            raise ImportError('div.source not found for ' + self.slug)
        sourcetext = sourceelem.text.strip()
        matches = re.match('^Source : ([^\/]*) /.*$',sourcetext)
        self.source = matches.group(1).strip()

    def __repr__(self):
        text =  self.level + ' ' + name
        text += + '\n\t cast time : ' + self.castTime
        text += + '\n\t duration : ' + self.duration
        text += + '\n\t school : ' + self.school
        text += + '\n\t compo : ' + self.compo
        text += + '\n\t range : ' + self.range
        text += + '\n\t ritual : ' + ('yes' if self.ritual else 'no')
        text += + '\n\t source : ' + self.source
        text += + '\n\n'