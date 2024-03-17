# The follow block of code setups the file pathing
# for Pytest module to run properly
import sys
import os

# Get the absolute path of the directory containing the current script (test_quiz.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the root directory
root_dir = os.path.dirname(current_dir)

# Add the root directory to the Python path
sys.path.append(root_dir)


import unittest
from applogic import SuperTicTacToe
import unittest

class TestSuperTicTacToe(unittest.TestCase):
    def test_create_game_initializes_board_correctly(self):
        game = SuperTicTacToe()
        gameid = 1
        game.create_game(gameid)
        self.assertEqual(len(game.board), 9)
        self.assertTrue(all(len(row) == 9 for row in game.board))
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.gameid, gameid)
        
    def test_make_move_valid_move(self):
        game = SuperTicTacToe()
        gameid = 1
        game.create_game(gameid)
        valid_move = game.make_move(gameid, 0, 0)
        self.assertTrue(valid_move)
        self.assertEqual(game.board[0][0], SuperTicTacToe.PLAYER_ONE)
        
    def test_make_move_invalid_move(self):
        game = SuperTicTacToe()
        gameid = 1
        game.create_game(gameid)
        game.make_move(gameid, 0, 0)  # First move
        invalid_move = game.make_move(gameid, 0, 0)  # Same spot
        self.assertFalse(invalid_move)
        
    def test_check_board_draw_not_draw(self):
        game = SuperTicTacToe()
        game.board = [[SuperTicTacToe.PLAYER_ONE] * 9] * 9
        self.assertFalse(game.check_board_draw())
        
    def test_check_board_draw_is_draw(self):
        game = SuperTicTacToe()
        game.board = [[SuperTicTacToe.PLAYER_ONE, SuperTicTacToe.PLAYER_TWO] * 4 + [SuperTicTacToe.PLAYER_ONE]] * 9
        self.assertTrue(game.check_board_draw())
        
    @patch('SuperTicTacToe().store.GameStateManager.save_game')
    def test_save_board(self, mock_save_game):
        game = SuperTicTacToe()
        gameid = 1
        game.create_game(gameid)
        game.save_board(gameid)
        mock_save_game.assert_called_once_with(gameid=gameid, turn=game.playerTurn, board=game.board)