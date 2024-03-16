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
from user import UserManager, User

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
        self.assertIsNone(self.user_manager.register_user("testuser", "password123"))

    def test_register_duplicate(self):
        """Test registering a user with a duplicate username."""
        self.user_manager.register_user("testuser", "password123")
        with self.assertRaises(Exception):
            self.user_manager.register_user("testuser", "newpassword")

    def test_login_valid(self):
        """Test logging in with valid credentials."""
        username = "validUser"
        password = "validPassword123"
        hashed_password = self.user_manager.hash_password(password)
        self.user_manager.register_user(username, hashed_password)  # Assume registration expects a hashed password
        result = self.user_manager.login_user(username, password)
        self.assertTrue(result, "Valid login should succeed")

    def test_login_invalid(self):
        """Test logging in with invalid credentials."""
        username = "validUser"
        password = "validPassword123"
        wrong_password = "wrongPassword123"
        hashed_password = self.user_manager.hash_password(password)
        self.user_manager.register_user(username, hashed_password)  # Register user with correct hashed password
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

    def test_get_all_users(self):
        """Test retrieving all usernames from the database."""
        # Register some users for the purpose of the test
        self.user_manager.register_user("testuser1", "password123")
        self.user_manager.register_user("testuser2", "password456")

        # Attempt to retrieve all usernames
        all_usernames = self.user_manager.get_all_users()

        # Verify the length of the usernames list
        self.assertEqual(len(all_usernames), 2)

        # Verify that the usernames retrieved match those registered
        self.assertIn("testuser1", all_usernames)
        self.assertIn("testuser2", all_usernames)

    def test_get_all_users_no_users(self):
        """Test retrieving all users from a database that has no users."""
        # Test retrieving all usernames when there are supposed to be no users
        all_usernames = self.user_manager.get_all_users()
        # Verify that the list of usernames is empty
        self.assertEqual(len(all_usernames), 0)

    def test_update_user_password_success(self):
        """Test successfully updating an existing user's password."""
        # First, register a user
        username, initial_password, new_password = "testuser", "initialPassword123", "newPassword456"
        self.user_manager.register_user(username, initial_password)

        # Now, attempt to update the user's password
        result = self.user_manager.update_user_password(username, new_password)
        self.assertTrue(result)  # Assert that the password update was successful

        # Optionally, verify the new password is set correctly by attempting to login
        login_success = self.user_manager.login_user(username, new_password)
        self.assertTrue(login_success)

    def test_update_user_password_failure_nonexistent_user(self):
        """Test attempting to update the password for a user that does not exist."""
        # Define a username and password for a user that has not been registered
        username, new_password = "nonexistentUser", "newPassword789"

        # Attempt to update the password for the non-existent user
        result = self.user_manager.update_user_password(username, new_password)
        self.assertFalse(result)  # Assert that the password update failed

    def test_hash_password_consistency(self):
        """Test that hashing the same password multiple times produces the same result."""
        password = "testPassword123"
        hash1 = self.user_manager.hash_password(password)
        hash2 = self.user_manager.hash_password(password)
        self.assertEqual(hash1, hash2, "Hashing the same password should always produce the same hash")

    def test_hash_password_uniqueness(self):
        """Test that hashing different passwords produces different results."""
        password1 = "passwordOne123"
        password2 = "passwordTwo123"
        hash1 = self.user_manager.hash_password(password1)
        hash2 = self.user_manager.hash_password(password2)
        self.assertNotEqual(hash1, hash2, "Hashing different passwords should produce different hashes")


if __name__ == '__main__':
    unittest.main()
