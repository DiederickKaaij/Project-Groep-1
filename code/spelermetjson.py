from commandmetjson import Command

class Speler:

    def __init__(self, huidigeLocatie, inventory):
        self.huidigeLocatie = huidigeLocatie
        self.inventory = inventory
    
    def command(self, commando):
        self.happening = Command(commando, self.huidigeLocatie, self.inventory)
        output = self.happening.isCommando()

        if isinstance(output, str):
            self.inventory.append(output)
        elif output > 0:
            self.huidigeLocatie = output
        
    def isWinst(self):
        return self.happening.locatie.locaties[self.huidigeLocatie-1]['win']