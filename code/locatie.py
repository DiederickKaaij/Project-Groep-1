class Locatie:

    def __init__(self, ID, naam, omschrijving,locked, 
                unlock_omschrijving, objecten, verbonden_met, win):
        self.ID = ID
        self.naam = naam
        self.omschrijving = omschrijving
        self.locked = locked
        self.unlock_omschrijving = unlock_omschrijving
        self.objecten = objecten
        self.verbonden_met = verbonden_met
        self.win = win
    
    