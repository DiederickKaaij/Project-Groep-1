from locatiemetjson import Locatie

class Command:
    
    def __init__(self, commando, loc, inv):
        self.commando = commando
        self.loc = loc
        self.locatie = Locatie()
        self.inv = inv

    def isCommando(self):
        if self.commando == "pick up sleutel":
            return self.pickUp()
        elif self.commando == "move hal":
            return self.move(1)
        elif self.commando == "move woonkamer":
            return self.move(2)
        elif self.commando == "move keuken":
            return self.move(3)
        elif self.commando == "look":
            return self.look()
        elif self.commando == "open":
            return self.open()
        else:
            print("Dit commando ken ik niet. Ik kan alleen move, look, open en pick up")
            return 0

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

    def look(self):
        print(self.locatie.locaties[self.loc-1]['omschrijving'])
        return 0

    def pickUp(self):
        if self.loc == 1:
            ding = self.locatie.geefObject("sleutel")
            print("je pakt de sleutel op")
            return ding
        else:
            print("hier ligt geen sleutel")
            return "stof"
    
    def open(self):
        if "sleutel" in self.inv and self.loc == 2:
            self.locatie.locaties[2]['locked'] = False
            print(self.locatie.locaties[2]['unlock_omschrijving'])
            return self.move(3)
        else:
            print("Je hebt de sleutel niet of bent niet bij de deur!")
            return 0