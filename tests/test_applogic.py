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
from store import GameStateManager

class TestSuperTicTacToe(unittest.TestCase):
    
    def test_create_game(self):
        game = SuperTicTacToe()
        GameStateManager().create_game('100')
        game.create_game('100')
        self.assertEqual(game.board, [[0 for _ in range(9)] for _ in range(9)])
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.gameid, '100')
    
    def test_make_move(self):
        game = SuperTicTacToe()
        GameStateManager().create_game('200')
        game.create_game('200')
        game.make_move('200', 0, 0)
        self.assertEqual(game.board[0][0], SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_TWO)
        game.make_move('200', 0, 0)
        self.assertEqual(game.board[0][0], SuperTicTacToe.PLAYER_ONE)
        self.assertEqual(game.playerTurn, SuperTicTacToe.PLAYER_TWO)
        
    def test_win_fill(self):
        game = SuperTicTacToe()
        GameStateManager().create_game('300')
        game.create_game('300')
        game.make_move('300', 0, 0) #player1
        print("testing text for test Player1:", game.board)
        game.make_move('300', 0, 8) #player2
        print("testing text for test Player2:", game.board)
        game.make_move('300', 0, 1) #player1
        print("testing text for test Player1:", game.board)
        game.make_move('300', 1, 8) #player2
        print("testing text for test Player2:", game.board)
        game.make_move('300', 0, 2) #player1
        print("testing text for test Player1:", game.board)
        game.make_move('300', 2, 8) #player2
        print("testing text for test Player2:", game.board)
        game.make_move('300', 0, 3) #player1
        print("testing text for test Player1:", game.board)
        game.make_move('300', 3, 8) #player1
        print("testing text for test Player1:", game.board)
        game.make_move('300', 0, 4) #player2
        print("testing text for test Player2:", game.board)    
        game.make_move('300', 4, 8) #player2
        print("testing text for test Player2:", game.board)
        game.make_move('300', 1, 0)
        game.make_move('300', 1, 7)
        game.make_move('300', 1, 1)
        game.make_move('300', 2, 7)
        game.make_move('300', 1, 2)
        game.make_move('300', 5, 8)
        game.make_move('300', 2, 0)
        game.make_move('300', 6, 8)
        game.make_move('300', 2, 1)
        game.make_move('300', 7, 8)
        game.make_move('300', 2, 2)
        self.assertEqual(game.board,[[1, 1, 1, 1, 1, 1, 1, 1, 1,]]*9)
        
    def test_diagonal_win(self):
        game = SuperTicTacToe()
        GameStateManager().create_game('400')
        game.create_game('400')
        game.make_move('400', 0, 0)
        game.make_move('400', 0, 7)
        game.make_move('400', 0, 4)
        game.make_move('400', 0, 1)
        game.make_move('400', 0, 8)
        self.assertEqual(game.board[0], [1]*9)
        
    def test_draw_fill(self):
        game = SuperTicTacToe()
        GameStateManager().create_game('500')
        game.create_game('500')
        game.make_move('500', 0, 0)
        print(game.board[0])
        game.make_move('500', 0, 1)
        print(game.board[0])
        game.make_move('500', 0, 2)
        print(game.board[0])
        game.make_move('500', 0, 3)
        print(game.board[0])
        game.make_move('500', 0, 5)
        print(game.board[0])
        game.make_move('500', 0, 8)
        print(game.board[0])
        game.make_move('500', 0, 7)
        print(game.board[0])
        game.make_move('500', 0, 6)
        print(game.board[0])
        game.make_move('500', 0, 4)
        print(game.board[0])
        self.assertEqual(game.board[0], [3]*9)
    
    def test_draw_game(self):
        
        game = SuperTicTacToe()
        GameStateManager().create_game('500')
        game.create_game('500')
        for i in range(7):
            game.make_move('500', i, 0)
            print("In Test:", game.board)
            game.make_move('500', i, 1)
            print("In Test:", game.board)
            game.make_move('500', i, 2)
            print("In Test:", game.board)
            game.make_move('500', i, 3)
            print("In Test:", game.board)
            game.make_move('500', i, 5)
            print("In Test:", game.board)
            game.make_move('500', i, 8)
            print("In Test:", game.board)
            game.make_move('500', i, 7)
            print("In Test:", game.board)
            game.make_move('500', i, 6)
            print("In Test:", game.board)
            game.make_move('500', i, 4)
            print("In Test:", game.board)
        print(game.board)
        self.assertEqual(game.check_game_draw(), True)
                      