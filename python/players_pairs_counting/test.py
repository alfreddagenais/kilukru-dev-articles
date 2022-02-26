import unittest
from count_player_pairs import count_player_pairs, possible_player_pairs

class TestPlayerPairsMethods(unittest.TestCase):
    def test_possibles(self):
        self.assertEqual(possible_player_pairs([]), [])
        self.assertEqual(possible_player_pairs(['A']), ['A'])
        self.assertEqual(possible_player_pairs(['A', 'B']), ['AB'])
        self.assertEqual(possible_player_pairs(['A', 'B', 'C']), ['AB', 'AC', 'BC'])
        self.assertEqual(possible_player_pairs(['A', 'B', 'C', 'D']), ['AB', 'AC', 'AD', 'BC', 'BD', 'CD'])

    def test_count_simple(self):
        self.assertEqual(count_player_pairs(0), 0)
        self.assertEqual(count_player_pairs(1), 1)
        self.assertEqual(count_player_pairs(2), 1)
        self.assertEqual(count_player_pairs(3), 3)
        self.assertEqual(count_player_pairs(4), 6)
        self.assertEqual(count_player_pairs(5), 10)
        self.assertEqual(count_player_pairs(6), 15)
        self.assertEqual(count_player_pairs(7), 21)
        self.assertEqual(count_player_pairs(10), 45)
        self.assertEqual(count_player_pairs(100), 4950)

    def test_count_large(self):
        self.assertEqual(count_player_pairs(1000), 499500)
        self.assertEqual(count_player_pairs(10000), 49995000)

if __name__ == "__main__":
    unittest.main()