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

    def test_canMove(self):
        self.command = Command("move hal", 2)
        result = self.command.canMove(1)
        self.assertTrue(result)

        self.assertFalse(self.command.canMove(3))

        self.command = Command("move hal", 3)
        self.assertFalse(self.command.canMove(1))

    def test_move(self):
        self.command = Command("move hal", 2)
        result = self.command.move(1)
        self.assertEqual(result, 1)

        result2 = self.command.move(3)
        self.assertEqual(result2, 0)

if __name__ == '__main__':
    unittest.main()