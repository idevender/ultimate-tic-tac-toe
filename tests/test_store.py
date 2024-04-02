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

    def test_create_game_pass(self):
        # Pass test for create_game
        self.setUp()
        self.manager.create_game()
        # If no exception is raised, the test passes

    def test_create_game_fail(self):
        # Fail test for create_game
        # Creating a game with the same ID should raise an IOError
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.create_game(game_id="id")

    def test_save_game_pass(self):
        # Pass test for save_game
        self.setUp()
        self.manager.create_game(game_id="test_game")
        self.manager.save_game("test_game", [], "player1", "player1")

    def test_save_game_fail(self):
        # Fail test for save_game
        # Saving a game with non-existent ID should raise an IOError
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.save_game("non_existent_game", [], "player1", "player1")

    def test_load_game(self):
        # Test loading a game state.
        self.setUp()
        self.manager.save_game("test_game")
        self.manager.load_game("test_game")

    def test_load_game_fail(self):
        # Test loading a game state that is not saved.
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.load_game("test_game")

    def test_remove_game(self):
        # Test removing a game state.
        self.setUp()
        self.manager.save_game("test_game")
        self.manager.remove_game("test_game")

    def test_remove_game_fail(self):
        # Test removing the game state that is not saved.
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.remove_game("test_game")


class TestUserManager(unittest.TestCase):

    def setUp(self):
        # Initialize a user manager
        self.db_name = 'test_users'
        self.manager = UserManager(self.db_name)

    def test_create_user(self):
        # Test creating a user
        self.setUp()
        self.manager.create_user("test_user","test_user_password")

    def test_create_user_fail(self):
        # Test creating a user that already exists
        self.setUp()
        self.manager.create_user("test_user","test_user_password")
        with self.assertRaises(IOError):
            self.manager.create_user("test_user","test_user_password")

    def test_save_user(self):
        # Test saving a user
        self.setUp()
        self.manager.create_user("test_user","test_user_password")
        self.manager.save_user("test_user", wins=1, losses=0 , draws=0)
    
    def test_save_user_fail(self):
        self.setUp()
        # Raise error when trying to update a user that doesn't exist.
        with self.assertRaises(IOError):
            self.manager.save_user("test_username", wins=1, losses=0 , draws=0)

    def test_load_user(self):
        self.setUp()
        # Test loading a user after creation.
        self.manager.create_user("test_user","test_password")
        self.manager.load_user("test_user")

    def test_load_user_fail(self):
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.load_user("test_user")

    def test_remove_user(self):
        # Test removing a user
        self.setUp()
        self.manager.create_user("test_user","test_user_password")
        self.manager.remove_user("test_user")

    def test_remove_user_fail(self):
        # Test removing a user that has not been saved.
        self.setUp()
        with self.assertRaises(IOError):
            self.manager.remove_user("test_user")

if __name__ == '__main__':
    unittest.main()