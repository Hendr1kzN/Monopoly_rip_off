import unittest
import player

class Player_tester(unittest.TestCase):

    def test_player(self):
        p1 = player.Player("Heni")
        self.assertEqual(p1.player_name, "Heni")
        self.assertEqual(p1.money, 1500)
        p1.add_money(100)
        self.assertEqual(p1.money, 1600)
        p1.give_money(100)
        self.assertEqual(p1.money, 1500)


if __name__ == '__main__':
    unittest.main()