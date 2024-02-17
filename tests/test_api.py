import sys
import os

# Get the absolute path of the directory containing the current script (test_quiz.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the root directory
root_dir = os.path.dirname(current_dir)

# Add the root directory to the Python path
sys.path.append(root_dir)

import unittest
from serverAPI import app
from webtest import TestApp

class YourClassTests(unittest.TestCase):
    def setUp(self):
        # Set up the app for testing
        self.app = TestApp(app)

    def test_get_homepage(self):
        # Test the get_homepage route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello World!")
    
    def test_verify_user(self):
        # Test the verify_user route
        response = self.app.get('/user')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "<h1> User Info </h1>")
        
    def test_update_user_info(self):
        # Test the update_user_info route
        response = self.app.post('/update_user/1')
        self.assertEqual(response.status_code, 200)
    
    def test_get_game_state(self):
        # Test the get_game_state route
        response = self.app.get('/load_game/1')
        self.assertEqual(response.status_code, 200)
        
    def test_update_game_state(self):
        # Test the update_game_state route
        response = self.app.post('/save_game/1')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
