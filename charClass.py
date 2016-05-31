from spellList import SpellList

class CharClass:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.spellList = SpellList(self.id)

    def __repr__(self):
        return {self.id: self.name}.__repr__()
