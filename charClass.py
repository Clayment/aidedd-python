from spellList import SpellList
import config 


class CharClass:
    def __init__(self, id, name):
		self.sPath = config.App.sPathToSave + '/' + id + '_' + name
    	
    	if not os.path.exists(self.sPath):
            os.makedirs(self.sPath)

        self.id = id
        self.name = name
        self.spellList = SpellList(self.id, self.sPath)

    def __repr__(self):
        return {self.id: self.name}.__repr__()
