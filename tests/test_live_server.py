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
import requests

class TestServerAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:8080'

    def test_get_homepage_redirect(self):
        response = requests.get(f'{self.BASE_URL}/')
        self.assertEqual(response.status_code, 302)

    def test_get_game_page(self):
        game_id = 'test_game_id'  # replace with a valid game_id
        response = requests.get(f'{self.BASE_URL}/game/{game_id}')
        self.assertEqual(response.status_code, 200)

    def test_get_login_page(self):
        response = requests.get(f'{self.BASE_URL}/login')
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        data = {'username': 'test', 'password': 'test'}  # replace with valid credentials
        response = requests.post(f'{self.BASE_URL}/login', data=data)
        self.assertEqual(response.status_code, 200)

    def test_update_user_info(self):
        username = 'test'  # replace with a valid username
        data = {'new_password': 'new_test'}  # replace with a new password
        response = requests.post(f'{self.BASE_URL}/update_user/{username}', data=data)
        self.assertEqual(response.status_code, 200)

    def test_get_register_user(self):
        response = requests.get(f'{self.BASE_URL}/register_user')
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        data = {'username': 'new_test', 'password': 'new_test'}  # replace with new credentials
        response = requests.post(f'{self.BASE_URL}/register_user', data=data)
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        user_id1 = 'test1'  # replace with a valid user_id
        user_id2 = 'test2'  # replace with a valid user_id
        response = requests.post(f'{self.BASE_URL}/create_game/{user_id1}/{user_id2}')
        self.assertEqual(response.status_code, 200)

    def test_check_game_state(self):
        game_id = 'test_game_id'  # replace with a valid game_id
        x = 0  # replace with a valid x coordinate
        y = 0  # replace with a valid y coordinate
        response = requests.get(f'{self.BASE_URL}/check_game/{game_id}/{x}/{y}')
        self.assertEqual(response.status_code, 200)

    def test_save_game_state(self):
        game_id = 'test_game_id'  # replace with a valid game_id
        response = requests.post(f'{self.BASE_URL}/save_game/{game_id}')
        self.assertEqual(response.status_code, 200)

    def test_load_game_state(self):
        game_id = 'test_game_id'  # replace with a valid game_id
        response = requests.get(f'{self.BASE_URL}/load_game/{game_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()