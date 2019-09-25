import unittest
from locatie import Locatie

class LocatieTest(unittest.TestCase):

    def setUp(self):
        self.locatie = Locatie(1, "hal", "Je staat in de hal.", True, "null","sleutel", 2, False)

    def test_ID(self):
        self.assertEqual(self.locatie.ID, 1)

    def test_naam(self):
        self.assertEqual(self.locatie.naam, "hal",)

    def test_omschrijving(self):
        self.assertEqual(self.locatie.omschrijving, "Je staat in de hal.")

    def test_locked(self):
        self.assertEqual(self.locatie.locked, True)

    def test_unlock_omschrijving(self):
        self.assertEqual(self.locatie.unlock_omschrijving, "null" )

    def test_objecten(self):
        self.assertEqual(self.locatie.objecten, "sleutel" )

    def test_verbonden_met(self):
        self.assertEqual(self.locatie.verbonden_met, 2 )
    
    def test_win(self):
        self.assertEqual(self.locatie.win, False )

if __name__ == '__main__':
    unittest.main()