import json

class Location:

    def __init__(self, plek):
        with open('speldata/locaties.json') as f:
            self.locaties = json.load(f)
        self.plek = plek

    
    def canMove(self):
        for x in self.locaties:
            if x['id'] == self.plek:
                return True

    def giveDescription(self):
        for x in self.locaties:
            if x['id'] == self.plek:
                return x['description']

    def isLocked(self):
        for x in self.locaties:
            if x['id'] == self.plek:
                i = 1
                for y in x['locked']:
                    if y:
                        richting = i
                    i += 1
                return richting