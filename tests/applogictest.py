import unittest
from applogic import SuperTicTacToe

class TestSuperTicTacToe(unittest.TestCase):

    def test_make_move(self):
        game = SuperTicTacToe()
        player = SuperTicTacToe.PLAYER_ONE
        row, col = 0, 0
        game.make_move(row, col, player)
        self.assertEqual(game.board[row][col], player, "The board did not update correctly after a move.")
        
    def test_check_game_draw(self):
        game = SuperTicTacToe()
        draw_board = [
            [[game.DRAW for _ in range(9)] for _ in range(9)]
        ]
        game.board = draw_board
        self.assertTrue(game.check_game_draw(), "The game did not recognize a draw.")