import unittest
from locatie import Locatie

class LocatieTest(unittest.TestCase):

    def setUp(self):
        self.locatie = Locatie(1, "hal")

    def test_ID(self):
        self.assertEqual(self.locatie.ID, 1)

    def test_naam(self):
        self.assertEqual(self.locatie.naam, "hal")


    
if __name__ == '__main__':
    unittest.main()