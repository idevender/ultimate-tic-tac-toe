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
    def test_create_game(self):
        game = SuperTicTacToe()
        game.create_game('100')
        self.assertEqual(game.board, [[0 for _ in range(9)] for _ in range(9)])
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.gameid, '100')
    
    def test_make_move(self):
        game = SuperTicTacToe()
        game.create_game('200')
        game.make_move('200', 0, 0)
        print(game.board)
        self.assertEqual(game.board[0][0], SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_TWO)
        game.make_move('200', 0, 0)
        self.assertEqual(game.board[0][0], SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_TWO)
        
    def test_win_fill(self):
        game = SuperTicTacToe()
        game.create_game('300')
        game.make_move('300', 0, 0)
        print(game.board)
        game.make_move('300', 0, 8)
        print(game.board)
        game.make_move('300', 0, 1)
        print(game.board)
        game.make_move('300', 1, 8)
        print(game.board)
        game.make_move('300', 0, 2)
        print(game.board)
        self.assertEqual(game.board,[[1, 1, 1, 1, 1, 1, 1, 1, 1,]]*9)
        
        
                      