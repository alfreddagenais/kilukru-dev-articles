import unittest
from game_matrix import GameMatrix


class TestPlayerPairsMethods(unittest.TestCase):
    def test_xsmall_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(2, 2)
        gameMatrix.position_init_player(0, 1)
        gameMatrix.position_init_hacker(1, 0)

        gameResult = gameMatrix.play_game()
        self.assertEqual(gameResult, [1, True])

    def test_small_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(10, 10)
        gameMatrix.position_init_player(0, 1)
        gameMatrix.position_init_hacker(9, 9)

        gameResult = gameMatrix.play_game()
        self.assertEqual(gameResult, [4, True])

    def test_medium_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(30, 30)
        gameMatrix.position_init_player(0, 1)
        gameMatrix.position_init_hacker(21, 15)

        gameResult = gameMatrix.play_game()
        self.assertLessEqual(gameResult[0], 7)
        self.assertEqual(gameResult[1], True)

    def test_tower_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(1, 80)
        gameMatrix.position_init_player(0, 1)
        gameMatrix.position_init_hacker(0, 71)

        gameResult = gameMatrix.play_game()
        self.assertEqual(gameResult, [7, True])

    def test_corridor_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(100, 1)
        gameMatrix.position_init_player(1, 0)
        gameMatrix.position_init_hacker(84, 0)

        gameResult = gameMatrix.play_game()
        self.assertEqual(gameResult, [7, True])

    def test_big_map(self):
        gameMatrix = GameMatrix()
        gameMatrix.create_matrix(100, 100)
        gameMatrix.position_init_player(0, 1)
        gameMatrix.position_init_hacker(21, 15)

        gameResult = gameMatrix.play_game()
        self.assertLessEqual(gameResult[0], 20)
        self.assertEqual(gameResult[1], True)


if __name__ == "__main__":
    unittest.main()
