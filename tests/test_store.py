import unittest
from ..store import GameStateManager, UserManager

class TestGameStateManager(unittest.TestCase):

    def setUp(self):
        # Initialize a game state manager
        self.db_name = 'test_gameStates'
        self.manager = GameStateManager(self.db_name)
        self.setUp()

    def test_setup_db(self):
        # Test the game state shelve setup, inital length should be 0.
        result = self.manager.setup_db()
        self.assertEqual(result, 0)

    def test_save_game(self):
        # Test saving a game state
        with self.assertRaises(IOError):
            self.manager.save_game("test_game")

    def test_load_game(self):
        # Test loading a game state
        with self.assertRaises(IOError):
            self.manager.load_game("test_game")

    def test_remove_game(self):
        # Test removing the game state
        with self.assertRaises(IOError):
            self.manager.remove_game("test_game")


class TestUserManager(unittest.TestCase):

    def setUp(self):
        # Initialize a user manager
        self.db_name = 'test_users'
        self.manager = UserManager(self.db_name)

    def test_setup_db(self):
        # Test the user shelve setup, inital length should be 0.
        result = self.manager.setup_db()
        self.assertEqual(result, 0)

    def test_save_user(self):
        # Test saving a user
        with self.assertRaises(IOError):
            self.manager.save_user("test_user")

    def test_load_user(self):
        # Test loading a user
        with self.assertRaises(IOError):
            self.manager.load_user("test_user")

    def test_remove_user(self):
        # Test removing a user
        with self.assertRaises(IOError):
            self.manager.remove_user("test_user")

if __name__ == '__main__':
    unittest.main()
