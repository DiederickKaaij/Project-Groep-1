import json

class Locatie:

    def __init__(self):
        with open('speldata/spelsimpel.json') as f:
            self.locaties = json.load(f)

    def geefObject(self, objectnaam):
        x_tel = 0
        for x in self.locaties:
            y_tel = 0
            for y in x['objecten']:
                if y == objectnaam:
                    return self.locaties[x_tel]['objecten'].pop(y_tel)
                y_tel += 1
            x_tel += 1
        