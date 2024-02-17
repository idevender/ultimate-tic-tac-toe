import unittest
from applogic import SuperTicTacToe  # Adjust this import to your file structure

class TestSuperTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = SuperTicTacToe()
    
    # Test make_move
    def test_make_move_valid(self):
        result = self.game.make_move(0, 0, SuperTicTacToe.PLAYER_ONE)
        self.assertTrue(result, "Move should be valid and accepted")

    def test_make_move_invalid(self):
        self.game.make_move(0, 0, SuperTicTacToe.PLAYER_ONE)
        result = self.game.make_move(0, 0, SuperTicTacToe.PLAYER_TWO)
        self.assertFalse(result, "Move should be invalid because the cell is already taken")

    # Assuming specific implementations for win and draw detection
    # Test check_board_draw
    def test_check_board_draw_true(self):
        # Fill the board with alternating player moves, ensuring no wins
        for i in range(9):
            for j in range(9):
                player = SuperTicTacToe.PLAYER_ONE if (i + j) % 2 == 0 else SuperTicTacToe.PLAYER_TWO
                self.game.make_move(i, j, player)
        self.assertTrue(self.game.check_board_draw(), "Board should be a draw")

    def test_check_board_draw_false(self):
        self.assertFalse(self.game.check_board_draw(), "Board should not be a draw initially")

    # Test draw_fill
    def test_draw_fill_board_state(self):
        self.game.draw_fill()
        for row in self.game.get_board():
            for cell in row:
                self.assertEqual(cell, SuperTicTacToe.DRAW, "All cells should indicate a draw")

    # Test win_fill
    def test_win_fill_player_one(self):
        self.game.win_fill(SuperTicTacToe.PLAYER_ONE)
        for row in self.game.get_board():
            for cell in row:
                self.assertEqual(cell, SuperTicTacToe.PLAYER_ONE, "All cells should be filled with PLAYER_ONE")

    def test_win_fill_player_two(self):
        self.game.win_fill(SuperTicTacToe.PLAYER_TWO)
        for row in self.game.get_board():
            for cell in row:
                self.assertEqual(cell, SuperTicTacToe.PLAYER_TWO, "All cells should be filled with PLAYER_TWO")

    # Additional tests to verify the state of the board after specific actions
    def test_get_board_initial_state(self):
        expected = [[SuperTicTacToe.PLAYABLE for _ in range(9)] for _ in range(9)]
        self.assertEqual(self.game.get_board(), expected, "Initial board state should be all zeros (playable)")

    def test_get_board_after_move(self):
        self.game.make_move(0, 0, SuperTicTacToe.PLAYER_ONE)
        result = self.game.get_board()
        self.assertEqual(result[0][0], SuperTicTacToe.PLAYER_ONE, "Board should reflect the move made by player one")

if __name__ == '__main__':
    unittest.main()
