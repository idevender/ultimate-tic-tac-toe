# The follow block of code setups the file pathing
# for Pytest module to run properly
import sys
import os
import unittest
# Get the absolute path of the directory containing the current script (test_quiz.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the root directory
root_dir = os.path.dirname(current_dir)

# Add the root directory to the Python path
sys.path.append(root_dir)



import unittest
from unittest.mock import patch, MagicMock
from bottle import Bottle, request, response
from webtest import TestApp
import serverAPI

import unittest
from webtest import TestApp
from unittest.mock import patch, MagicMock
import serverAPI
import applogic
import frontend

class TestServerAPI(unittest.TestCase):

    def setUp(self):
        self.app = TestApp(serverAPI.app)

    @patch('serverAPI.redirect')
    def test_get_homepage(self, mock_redirect):
        mock_redirect.return_value = 'Redirected'
        response = self.app.get('/')
        mock_redirect.assert_called_once_with('/login')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Redirected')

    @patch('serverAPI.applogic.SuperTicTacToe')
    @patch('serverAPI.frontend.RenderEngine')
    def test_get_game_page_success(self, mock_frontend, mock_applogic):
        game_id = 'test_game_id'
        mock_applogic.return_value.load_board.return_value = True
        mock_frontend.return_value.render_main_game_page.return_value = 'Game Page'
        response = self.app.get(f'/game/{game_id}')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Game Page')

    @patch('serverAPI.applogic.SuperTicTacToe')
    @patch('serverAPI.frontend.RenderEngine')
    def test_get_game_page_failure(self, mock_frontend, mock_applogic):
        game_id = 'test_game_id'
        mock_applogic.return_value.load_board.return_value = False
        mock_frontend.return_value.render_main_game_page.return_value = 'Game Page'
        response = self.app.get(f'/game/{game_id}', expect_errors=True)
        self.assertEqual(response.status, '404 Not Found')

    @patch('serverAPI.frontend.RenderEngine')
    def test_get_login_page_success(self, mock_frontend):
        mock_frontend.return_value.render_login_page.return_value = 'Login Page'
        response = self.app.get('/login')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Login Page')

    @patch('serverAPI.frontend.RenderEngine')
    def test_get_login_page_failure(self, mock_frontend):
        mock_frontend.return_value.render_login_page.return_value = False
        response = self.app.get('/login', expect_errors=True)
        self.assertNotEqual(response.status, '200 OK')
        
    @patch('serverAPI.user.UserManager.login_user')
    @patch('serverAPI.frontend.RenderEngine')
    @patch('serverAPI.user.UserManager.get_user_history')
    def test_login_user_success(self, mock_get_user_history, mock_frontend, mock_login_user):
        mock_login_user.return_value = True
        mock_frontend.return_value.render_user_page.return_value = 'User Page'
        response = self.app.post('/login', params={'username': 'test', 'password': 'test'})
        self.assertEqual(response.status, '200 OK')
        mock_get_user_history.assert_called_once_with('test')

    @patch('serverAPI.user.UserManager.login_user')
    def test_login_user_failure(self, mock_login_user):
        mock_login_user.return_value = None
        response = self.app.post('/login', params={'username': 'test', 'password': 'test'}, expect_errors=True)
        self.assertEqual(response.status, '404 Not Found')
        self.assertEqual(response.body, b'User not found')
    
    @patch('serverAPI.user.UserManager.update_user_password')
    def test_update_user_info_success(self, mock_update_user_password):
        mock_update_user_password.return_value = True
        response = self.app.post('/update_user/test', params={'new_password': 'test'})
        self.assertEqual(response.status, '200 OK')

    @patch('serverAPI.user.UserManager.update_user_password')
    def test_update_user_info_failure(self, mock_update_user_password):
        mock_update_user_password.return_value = False
        response = self.app.post('/update_user/test', params={'new_password': 'test'}, expect_errors=True)
        self.assertEqual(response.status, '404 Not Found')
    
    @patch('serverAPI.frontend.RenderEngine.render_signup_page')
    def test_get_register_user_success(self, mock_render_signup_page):
        mock_render_signup_page.return_value = 'Signup Page'
        response = self.app.get('/register_user')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Signup Page')

    @patch('serverAPI.frontend.RenderEngine.render_signup_page')
    def test_get_register_user_failure(self, mock_render_signup_page):
        mock_render_signup_page.return_value = None
        response = self.app.get('/register_user', expect_errors=True)
        self.assertEqual(response.status, '404 Not Found')
        self.assertEqual(response.body, b'Page Not Found')
        
    @patch('serverAPI.user.UserManager.register_user')
    @patch('serverAPI.frontend.RenderEngine.render_main_game_page')
    def test_register_user_success(self, mock_render_main_game_page, mock_register_user):
        mock_register_user.return_value = True
        mock_render_main_game_page.return_value = 'Main Game Page'
        user_data = {'username': 'test', 'password': 'test'}
        response = self.app.post('/register_user', params=user_data)
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Main Game Page')

    @patch('serverAPI.user.UserManager.register_user')
    def test_register_user_failure(self, mock_register_user):
        mock_register_user.return_value = False
        user_data = {'username': 'test', 'password': 'test'}
        response = self.app.post('/register_user', params=user_data, expect_errors=True)
        self.assertEqual(response.status, '400 Bad Request')
        self.assertEqual(response.body, b'User already exists')

    @patch('serverAPI.user.UserManager.gen_game_id')
    @patch('serverAPI.applogic.SuperTicTacToe.create_game')
    @patch('serverAPI.applogic.SuperTicTacToe.load_board')
    @patch('serverAPI.frontend.RenderEngine.render_main_game_page')
    def test_create_game_success(self, mock_render_main_game_page, mock_load_board, mock_create_game, mock_gen_game_id):
        mock_gen_game_id.return_value = 'game_id'
        mock_load_board.return_value = 'game_board'
        mock_render_main_game_page.return_value = 'Main Game Page'
        response = self.app.post('/create_game/user1/user2')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Main Game Page')

    @patch('serverAPI.user.UserManager.gen_game_id')
    @patch('serverAPI.applogic.SuperTicTacToe.create_game')
    @patch('serverAPI.applogic.SuperTicTacToe.load_board')
    @patch('serverAPI.frontend.RenderEngine.render_main_game_page')
    def test_create_game_failure(self, mock_render_main_game_page, mock_load_board, mock_create_game, mock_gen_game_id):
        mock_gen_game_id.return_value = 'game_id'
        mock_load_board.return_value = None
        mock_render_main_game_page.return_value = 'Error Page'
        response = self.app.post('/create_game/user1/user2', expect_errors=True)
        self.assertEqual(response.status, '500 Internal Server Error')
        self.assertEqual(response.body, b'Error Page')
        
    @patch('serverAPI.applogic.SuperTicTacToe.make_move')
    @patch('serverAPI.applogic.SuperTicTacToe.load_board')
    @patch('serverAPI.frontend.RenderEngine.render_updated_board')
    def test_check_game_state_success(self, mock_render_updated_board, mock_load_board, mock_make_move):
        mock_make_move.return_value = True
        mock_load_board.return_value = 'game_board'
        mock_render_updated_board.return_value = 'Updated Board'
        response = self.app.get('/check_game/game_id/1/1')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Updated Board')

    @patch('serverAPI.applogic.SuperTicTacToe.make_move')
    def test_check_game_state_failure(self, mock_make_move):
        mock_make_move.return_value = False
        response = self.app.get('/check_game/game_id/1/1', expect_errors=True)
        self.assertEqual(response.status, '400 Bad Request')
        self.assertEqual(response.body, b'Invalid Move')

    @patch('serverAPI.applogic.SuperTicTacToe.save_board')
    def test_save_game_state_success(self, mock_save_board):
        mock_save_board.return_value = True
        response = self.app.post('/save_game/game_id')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Game Saved')

    @patch('serverAPI.applogic.SuperTicTacToe.save_board')
    def test_save_game_state_failure(self, mock_save_board):
        mock_save_board.return_value = False
        response = self.app.post('/save_game/game_id', expect_errors=True)
        self.assertEqual(response.status, '400 Bad Request')

    @patch('serverAPI.applogic.SuperTicTacToe.load_board')
    @patch('serverAPI.frontend.RenderEngine.render_updated_board')
    def test_load_game_state_success(self, mock_render_updated_board, mock_load_board):
        mock_load_board.return_value = 'game_board'
        mock_render_updated_board.return_value = 'Rendered Board'
        response = self.app.get('/load_game/game_id')
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.body, b'Rendered Board')

    @patch('serverAPI.applogic.SuperTicTacToe.load_board')
    def test_load_game_state_failure(self, mock_load_board):
        mock_load_board.return_value = None
        response = self.app.get('/load_game/game_id', expect_errors=True)
        self.assertEqual(response.status, '404 Not Found')
        self.assertEqual(response.body, b'Game Not Found')

if __name__ == '__main__':
    unittest.main()
    
#write a success and failure unit test for the selected code