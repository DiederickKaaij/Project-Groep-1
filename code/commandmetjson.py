from locatiemetjson import Locatie

class Command:
    
    def __init__(self, commando, loc):
        self.commando = commando
        self.loc = loc
        self.locatie = Locatie()

    def isCommando(self):
        if self.commando == "pick up key":
            return True
        elif self.commando == "move hal":
            return True
        elif self.commando == "move woonkamer":
            return True
        elif self.commando == "move keuken":
            return True
        elif self.commando == "look":
            return True
        elif self.commando == "open":
            return True
        else:
            return False

    def canMove(self, bestemming):
        for y in self.locatie.locaties:
            if y['id'] == bestemming:
                if y['locked']:
                    print("De deur zit op slot!")
                    return False

        for x in self.locatie.locaties:
            if x['id'] == self.loc:
                verbindingen = x['verbonden_met']

        return bestemming in verbindingen

    def move(self, bestemming):
        if self.canMove(bestemming):
            print(self.locatie.locaties[bestemming-1]['omschrijving'])
            return bestemming
        else:
            print("Je kunt daar niet heen")
            return 0