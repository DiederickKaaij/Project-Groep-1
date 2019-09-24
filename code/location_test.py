import unittest
from location import Location

class LocationTest(unittest.TestCase):

    def setUp(self):
        self.locatie = Location([1,0])

    def test_init(self):
        result = self.locatie.plek
        self.assertEqual(result, [1,0])

    def test_canmove(self):
        result = self.locatie.canMove()
        self.assertTrue(result)

    def test_givedescription(self):
        result = self.locatie.giveDescription()
        self.assertEqual(result, "You are standing in your cell. It is very barebones, aside from a poster on the east wall.")

    def test_islocked(self):
        result = self.locatie.isLocked()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
