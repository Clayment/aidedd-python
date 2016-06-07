from spellList import SpellList
import config 


class CharClass:
    def __init__(self, _id, name):
        self.sPath = config.App.sPathToSave + '/' + _id + '_' + name

        self.id = _id
        self.name = name
        self.spellList = SpellList(self.id, self.sPath)

    def __repr__(self):
        return {self.id: self.name}.__repr__()
