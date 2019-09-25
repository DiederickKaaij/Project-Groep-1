import unittest
from commandmetjson import Command

class TestCommand(unittest.TestCase):

    def test_init(self):
        self.command = Command("move", 1)
        self.assertEqual(self.command.commando, "move")
        self.assertEqual(self.command.loc, 1)

    def test_isCommando(self):
        self.command = Command("pick up key", 1)
        self.assertTrue(self.command.isCommando())

        self.command = Command("look", 1)
        self.assertTrue(self.command.isCommando())

        self.command = Command("bullshit", 1)
        self.assertFalse(self.command.isCommando())

if __name__ == '__main__':
    unittest.main()