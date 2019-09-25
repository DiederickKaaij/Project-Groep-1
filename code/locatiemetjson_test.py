import unittest
from locatiemetjson import Locatie

class LocatieTest(unittest.TestCase):

    def setUp(self):
        self.locatie = Locatie()

    def test_init(self):
        self.assertEqual(self.locatie.locaties[0]['id'], 1)
        self.assertEqual(self.locatie.locaties[1]['naam'], "woonkamer")
        self.assertEqual(self.locatie.locaties[2]['omschrijving'], "Je bent in de keuken. Eindelijk eten!")
        self.assertTrue(self.locatie.locaties[2]['locked'])
        self.assertIsNone(self.locatie.locaties[0]['unlock_omschrijving'])
        self.assertEqual(self.locatie.locaties[0]['objecten'], ["sleutel"])
        self.assertEqual(self.locatie.locaties[1]['verbonden_met'], [1,3])
        self.assertFalse(self.locatie.locaties[0]['win'])

    def test_geefobject(self):
        result = self.locatie.geefObject("sleutel")
        self.assertEqual(result, "sleutel")
        self.assertFalse(self.locatie.locaties[0]['objecten'])

if __name__ == '__main__':
    unittest.main()