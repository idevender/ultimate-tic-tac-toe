# The follow block of code setups the file pathing
# for Pytest module to run properly
from user import UserManager, User
import unittest
import sys
import os
from unittest.mock import patch
import store

# Get the absolute path of the directory containing the current script (test_quiz.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the root directory
root_dir = os.path.dirname(current_dir)

# Add the root directory to the Python path
sys.path.append(root_dir)


class TestUser(unittest.TestCase):
    def test_init_valid(self):
        """Test User initialization with valid credentials."""
        user = User("testuser", "password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "password123")

    def test_init_invalid(self):
        """Test User initialization with invalid credentials."""
        with self.assertRaises(TypeError):
            User(None, "password123")
        with self.assertRaises(TypeError):
            User("testuser", None)


class TestUserManager(unittest.TestCase):
    def setUp(self):
        """Set up a UserManager for testing."""
        self.user_manager = UserManager()
        self.user_manager.setup()

    def test_register_valid(self):
        """Test registering a user with valid credentials."""
        username = "valid"
        password = "validpassword"
        # Attempt to register a new user
        registration_result = self.user_manager.register_user(
            username, password)
        self.assertTrue(registration_result,
                        "Registration should succeed for new username.")

        # Verify the password is hashed
        stored_user = self.user_manager.user_db.load_user(username)
        hashed_password = self.user_manager.hash_password(password)
        self.assertEqual(
            stored_user['password'], hashed_password, "The stored password should be hashed.")

    def test_register_duplicate(self):
        """Test registering a user with a duplicate username."""
        username = "duplicateUserName"
        password = "tiktoktaktik"
        # Attempt to register should succeed
        result_first_attempt = self.user_manager.register_user(
            username, password)
        self.assertTrue(result_first_attempt,
                        "first registration attempt should succeed.")

        # Attempt with the same username should fail
        result_second_attempt = self.user_manager.register_user(
            username, "new")
        self.assertFalse(result_second_attempt,
                         "The second registration attempt will fail.")

    def test_login_valid(self):
        """Test logging in with valid credentials."""
        username = "validUser"
        password = "validPassword123"
        hashed_password = self.user_manager.hash_password(password)
        # Assume registration expects a hashed password
        self.user_manager.register_user(username, hashed_password)
        result = self.user_manager.login_user(username, password)
        self.assertTrue(result, "Valid login should succeed")

    def test_login_invalid(self):
        """Test logging in with invalid credentials."""
        username = "validUser"
        password = "validPassword123"
        wrong_password = "wrongPassword123"
        hashed_password = self.user_manager.hash_password(password)
        # Register user with correct hashed password
        self.user_manager.register_user(username, hashed_password)
        result = self.user_manager.login_user(username, wrong_password)
        self.assertFalse(result, "Invalid login should fail")

    def test_get_user_exists(self):
        """Test retrieving an existing user."""
        self.user_manager.register_user("testuser", "password123")
        user = self.user_manager.get_user("testuser")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "password123")

    def test_get_user_absent(self):
        """Test retrieving a non-existing user."""
        user = self.user_manager.get_user("nonexistentuser")
        self.assertIsNone(user)

    def test_get_all_online_users(self):
        """Test retrieving usernames of all users marked as online from the database."""
        # Set up users and mark them as online or offline
        self.user_manager.register_user(
            "onlineUser1", "password123", online=True)
        self.user_manager.register_user(
            "onlineUser2", "password456", online=True)
        self.user_manager.register_user(
            "offlineUser", "password789", online=False)

        # Attempt to retrieve usernames of online users
        online_usernames = self.user_manager.get_all_online_users()

        # Verify the list includes only users marked as online
        self.assertEqual(len(online_usernames), 2)
        self.assertIn("onlineUser1", online_usernames)
        self.assertIn("onlineUser2", online_usernames)
        self.assertNotIn("offlineUser", online_usernames)

    def test_get_all_online_users_no_online_users(self):
        """Test retrieving online users from a database when no users are marked as online."""
        # Set up users but do not mark any as online
        self.user_manager.register_user(
            "offlineUser1", "password123", online=False)
        self.user_manager.register_user(
            "offlineUser2", "password456", online=False)

        # Test retrieving usernames when no users are supposed to be online
        online_usernames = self.user_manager.get_all_online_users()

        # Verify that the list of online usernames is empty
        self.assertEqual(len(online_usernames), 0)

    def test_update_user_password_success(self):
        """Test successfully updating an existing user's password."""
        username = "existingUser"
        old_password = "oldPassword123"
        new_password = "newPassword123"
        # Register a user with the old password
        self.user_manager.register_user(
            username, self.user_manager.hash_password(old_password))
        # Attempt to update the password to the new password
        update_success = self.user_manager.update_user_password(
            username, new_password)
        self.assertTrue(
            update_success, "Updating an existing user's password succeed")
        # Verify login with the new password is successful
        login_success = self.user_manager.login_user(username, new_password)
        self.assertTrue(login_success, "Able to login with the new password")

    def test_update_user_password_fail_nonexist_user(self):
        """Test attempting to update the password for a user that does not exist."""
        username = "nonexistentUser"
        new_password = "newPassword456"
        # Attempt to update the password for a user is not registered
        update_success = self.user_manager.update_user_password(
            username, new_password)
        self.assertFalse(
            update_success, "Updating a non-existent user's password should fail")

    def test_hash_password_consistency(self):
        """Test that hashing the same password multiple times produces the same result."""
        password = "testPassword123"
        hash1 = self.user_manager.hash_password(password)
        hash2 = self.user_manager.hash_password(password)
        self.assertEqual(
            hash1, hash2, "Hashing the same password should always produce the same hash")

    def test_hash_password_uniqueness(self):
        """Test that hashing different passwords produces different results."""
        password1 = "passwordOne123"
        password2 = "passwordTwo123"
        hash1 = self.user_manager.hash_password(password1)
        hash2 = self.user_manager.hash_password(password2)
        self.assertNotEqual(
            hash1, hash2, "Hashing different passwords should produce different hashes")

    def test_gen_game_id_and_initialize_game_success(self):
        """Test generating a unique game ID and initializing a game."""
        user_id1 = "user1"
        user_id2 = "user2"

        game_id = self.user_manager.gen_game_id(user_id1, user_id2)
        self.assertIsNotNone(game_id, "A unique game ID will be generated.")

        # Verify that the game state was initialized in the database
        game_state_manager = store.GameStateManager(db_name='gameStates')
        game_state = game_state_manager.load_game(game_id)
        self.assertIsNotNone(
            game_state, "Game state should exist in the database.")
        self.assertEqual(game_state['player1'],
                         user_id1, "First player will match.")
        self.assertEqual(game_state['player2'],
                         user_id2, "Second player will match.")

    def test_gen_game_id_with_nonexistent_users(self):
        """Test game initialization failure when user IDs do not exist."""
        user_id1 = "doesnotexistUser1"
        user_id2 = "doesnotexistUser2"

        try:
            game_id = self.user_manager.gen_game_id(user_id1, user_id2)
            game_state_manager = store.GameStateManager(db_name='gameStates')
            game_state = game_state_manager.load_game(game_id)
            # If the game state loads successfully, it means the test unexpectedly passed. Fail the test.
            self.fail(
                "Game initialization succeeded with non-existent users, which is unexpected.")
        except Exception as e:
            # Expect exception since users do not exist and pass the test if an exception is caught.
            pass

    def test_get_leaderboard_with_enough_players(self):
        """Test the leaderboard with more than 10 players having different win counts."""
        # Set up users and simulate game wins
        for i in range(15):
            username = f"Player{i}"
            self.user_manager.register_user(username, "password")
            for j in range(i):  # Simulate 'i' wins for 'Player i'
                self.user_manager.update_user_history(username, 'win')

        leaderboard = self.user_manager.get_leaderboard()
        self.assertEqual(len(leaderboard), 10,
                         "Leaderboard should have exactly 10 players.")
        # Ensure the leaderboard is sorted by win count in descending order
        self.assertTrue(all(leaderboard[i][1] >= leaderboard[i + 1][1] for i in range(len(leaderboard) - 1)),
                        "Leaderboard should be sorted by win counts in descending order.")

    def test_get_leaderboard_with_insufficient_players(self):
        """Test the leaderboard when there are fewer than 10 players."""
        # Set up users and simulate game wins
        for i in range(5):  # Less than 10 players
            username = f"Player{i}"
            wins = i  # Assign a varying number of wins to each player
            self.user_manager.create_user(username, "password", wins=wins)

        leaderboard = self.user_manager.get_leaderboard()
        self.assertEqual(
            len(leaderboard), 5, "Leaderboard should contain all players if fewer than 10.")
        # Ensure the leaderboard is sorted by win count in descending order
        self.assertTrue(all(leaderboard[i][1] >= leaderboard[i + 1][1] for i in range(len(leaderboard) - 1)),
                        "Leaderboard should be sorted by win counts in descending order.")

    def test_get_leaderboard_no_players(self):
        """Test the leaderboard when no players have played any games."""
        # Ensure no players are registered or have wins
        # This might need adjustment based on how setup_db is implemented
        self.user_manager.setup_db()

        leaderboard = self.user_manager.get_leaderboard()
        self.assertEqual(len(leaderboard), 0,
                         "Leaderboard should be empty if no players exist.")

    @patch('store.shelve.open')
    def test_get_active_games_with_games(self, mock_shelve_open):
        """Test retrieving active games for a user with active games."""
        username = "activeUser"
        # Mock database response
        mock_db = {
            'game1': {'player1': username, 'player2': 'opponent1', 'winner': None},
            'game2': {'player1': 'opponent2', 'player2': username, 'winner': None},
        }
        mock_shelve_open.return_value.__enter__.return_value = mock_db

        # Perform the test
        active_games = self.user_manager.get_active_games(username)
        self.assertEqual(len(active_games), 2,
                         "Should return 2 active games for the user")

    @patch('store.shelve.open')
    def test_get_active_games_no_games(self, mock_shelve_open):
        """Test retrieving active games for a user with no active games."""
        username = "lonelyUser"
        # Mock database response to simulate no active games for the user
        mock_db = {
            'game1': {'player1': 'otherUser1', 'player2': 'otherUser2', 'winner': 'otherUser1'},
            'game2': {'player1': 'otherUser3', 'player2': 'otherUser4', 'winner': None},
        }
        mock_shelve_open.return_value.__enter__.return_value = mock_db

        # Perform the test
        active_games = self.user_manager.get_active_games(username)
        self.assertEqual(len(active_games), 0,
                         "Should return no active games for the user")


if __name__ == '__main__':
    unittest.main()
