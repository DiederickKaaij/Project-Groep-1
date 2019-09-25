from locatiemetjson import Locatie

class Command:
    
    def __init__(self, commando, loc):
        self.commando = commando
        self.loc = loc

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