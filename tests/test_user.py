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
        self.user_manager.register_user("testuser", "password123")
        self.assertTrue(self.user_manager.login_user("testuser", "password123"))

    def test_login_invalid(self):
        """Test logging in with invalid credentials."""
        self.user_manager.register_user("testuser", "password123")
        self.assertFalse(self.user_manager.login_user("testuser", "wrongpassword"))

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

    def test_get_all_users_with_users(self):
        """Test retrieving all users from a database that has users."""
        # Assume the registration process works correctly for this test
        self.user_manager.register_user("testuser1", "password123")
        self.user_manager.register_user("testuser2", "password456")

        # Retrieve all users
        all_users = self.user_manager.get_all_users()

        # Verify the number of users matches what was registered
        self.assertEqual(len(all_users), 2)

        # Verify the content matches the registered users
        expected_usernames = {"testuser1", "testuser2"}
        retrieved_usernames = {user.username for user in all_users}
        self.assertTrue(expected_usernames.issubset(retrieved_usernames))

    def test_get_all_users_no_users(self):
        """Test retrieving all users from a database that has no users."""
        # Test the method when no users have been registered
        all_users = self.user_manager.get_all_users()

        # The list of all users should be empty
        self.assertEqual(len(all_users), 0)

if __name__ == '__main__':
    unittest.main()
