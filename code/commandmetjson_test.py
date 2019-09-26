import unittest
from commandmetjson import Command

class TestCommand(unittest.TestCase):

    def test_init(self):
        self.command = Command("move", 1, [""])
        self.assertEqual(self.command.commando, "move")
        self.assertEqual(self.command.loc, 1)

    # def test_isCommando(self):
    #     self.command = Command("pick up key", 1,[""])
    #     self.assertTrue(self.command.isCommando())

    #     self.command = Command("look", 1, [""])
    #     self.assertTrue(self.command.isCommando())

    #     self.command = Command("bullshit", 1, [""])
    #     self.assertFalse(self.command.isCommando())

    def test_isCommandobeter(self):
        self.command = Command("pick up sleutel", 2, [""])
        self.assertEqual(self.command.isCommando(), "sleutel")

        self.command = Command("move hal", 2, [""])
        self.assertEqual(self.command.isCommando(), 1)

        self.command = Command("move keuken", 1, [""])
        self.assertEqual(self.command.isCommando(), 0)

        self.command = Command("move woonkamer", 1, [""])
        self.assertEqual(self.command.isCommando(), 2)

        self.command = Command("look", 3, [""])
        self.assertEqual(self.command.isCommando(), 0)

        self.command = Command("open", 2, ["sleutel"])
        self.assertEqual(self.command.isCommando(), 0)
        self.assertEqual(self.command.locatie.locaties[2]['locked'], False)

        self.command = Command("bullshit", 1, [""])
        self.assertEqual(self.command.isCommando(), 0)

    def test_canMove(self):
        self.command = Command("move hal", 2, [""])
        result = self.command.canMove(1)
        self.assertTrue(result)

        self.assertFalse(self.command.canMove(3))

        self.command = Command("move hal", 3, [""])
        self.assertFalse(self.command.canMove(1))

    def test_move(self):
        self.command = Command("move hal", 2, [""])
        result = self.command.move(1)
        self.assertEqual(result, 1)

        result2 = self.command.move(3)
        self.assertEqual(result2, 0)

    def test_look(self):
        self.command = Command("look", 3,[""])
        self.assertEqual(self.command.look(), 0)

    def test_pickUp(self):
        self.command = Command("pick up key", 1,[""])
        self.assertEqual(self.command.pickUp(), "sleutel")

    def test_open(self):
        self.command = Command("open", 2, ["sleutel"])
        self.assertEqual(self.command.open(), 0)

if __name__ == '__main__':
    unittest.main()