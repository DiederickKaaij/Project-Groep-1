from spelermetjson import Speler

class Game:

    def __init__(self):
        self.gewonnen = False
        self.speler = Speler(1,[""])
        self.speler.command("look")

    def run(self):
        while self.gewonnen == False:
            cmd = input()
            self.speler.command(cmd)

            self.gewonnen = self.speler.isWinst()
            if self.gewonnen:
                print("Je hebt gewonnnen! Gefeliciteerd")

newGame = Game()
newGame.run()
