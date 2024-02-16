import unittest
from user import UserManager

class TestUserManager(unittest.TestCase):

    def test_register_user(self):
        manager = UserManager()
        manager.register_user("test_user", "password")
        # Add assertions to verify if the user is properly registered.
        self.assertIsNotNone(manager.get_user("test_user"))

    def test_login_user(self):
        manager = UserManager()
        # Test successful login
        self.assertTrue(manager.login_user("admin", "admin"))
        # Test unsuccessful login
        self.assertFalse(manager.login_user("non_existing_user", "password"))

    def test_get_user(self):
        manager = UserManager()
        # Add a user to the system
        manager.register_user("test_user", "password")
        # Test if the added user can be retrieved
        user = manager.get_user("test_user")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "test_user")

if __name__ == '__main__':
    unittest.main()
