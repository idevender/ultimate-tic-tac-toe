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
from store import GameStateManager, UserManager

class TestGameStateManager(unittest.TestCase):

    def setUp(self):
        # Initialize a game state manager
        self.db_name = 'test_gameStates'
        self.manager = GameStateManager(self.db_name)

    def test_setup_db(self):
        # Test the game state shelve setup, inital length should be 0.
        result = self.manager.setup_db()
        self.assertEqual(result, 0)

    def test_save_game(self):
        self.setUp()
        # Test saving a game state
        with self.assertRaises(IOError):
            self.manager.save_game("test_game")

    def test_save_game_fail(self):
        self.setUp()
        self.manager.save_game("test_game")
        # Raise error on second save attempt since game is already saved.
        with self.assertRaises(IOError):
            self.manager.save_game("test_game")


    def test_load_game(self):
        # Test loading a game state.
        self.setUp()
        self.manager.save_game("test_game")
        self.manager.load_game("test_game")

    def test_load_game_fail(self):
        # Test loading a game state that is not saved.
        with self.assertRaises(IOError):
            self.manager.load_game("test_game")

    def test_remove_game(self):
        # Test removing a game state.
        self.setUp()
        self.manager.save_game("test_game")
        self.manager.remove_game("test_game")

    def test_remove_game_fail(self):
        # Test removing the game state that is not saved.
        with self.assertRaises(IOError):
            self.manager.remove_game("test_game")


class TestUserManager(unittest.TestCase):

    def setUp(self):
        # Initialize a user manager
        self.db_name = 'test_users'
        self.manager = UserManager(self.db_name)

    def test_setup_db(self):
        self.setUp()
        # Test the user shelve setup, inital length should be 0.
        result = self.manager.setup_db()
        self.assertEqual(result, 0)

    def test_save_user(self):
        # Test saving a user
        self.setUp()
        self.manager.save_user("test_user","test_user_password")
    
    def test_save_user_fail(self):
        self.setUp()
        self.manager.save_user("test_user","test_user_password")
        # Raise error on second save attempt since user is already saved.
        with self.assertRaises(IOError):
            self.manager.save_user("test_user","test_user_password")

    def test_load_user(self):
        # Test loading a user after save
        self.setUp()
        self.manager.save_user("test_user","test_password")
        self.manager.load_user("test_user")

    def load_user_fail(self):
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.load_user("test_user")

    def test_remove_user(self):
        # Test removing a user
        self.setUp()
        self.manager.save_user("test_user","test_user_password")
        self.manager.remove_user("test_user")

    def test_remove_user_fail(self):
        # Test removing a user that has not been saved.
        with self.assertRaises(IOError):
            self.manager.remove_user("test_user")
