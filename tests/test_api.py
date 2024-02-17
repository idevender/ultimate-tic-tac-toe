import unittest
from unittest.mock import patch, MagicMock
from bottle import Bottle, request, response
import serverAPI

class TestServerAPI(unittest.TestCase):
    @patch('serverAPI.html')
    @patch('serverAPI.applogic')
    @patch('serverAPI.user')
    def setUp(self, mock_user, mock_applogic, mock_html):
        self.mock_user = mock_user
        self.mock_applogic = mock_applogic
        self.mock_html = mock_html
        self.app = serverAPI.app

    def test_get_homepage(self):
        result = self.app.get('/')
        self.assertEqual(result, "Hello World!")

    def test_get_game_page(self):
        self.mock_applogic.SuperTicTacToe.get_board.return_value = 'board'
        self.mock_html.load_game_page.return_value = 'game page'
        result = self.app.get('/game/1')
        self.assertEqual(result, 'game page')

    def test_verify_user(self):
        self.mock_user.UserManager.login_user.return_value = True
        request.forms = {'username': 'test', 'password': 'test'}
        result = self.app.get('/user')
        self.assertEqual(response.status_code, 200)

    @patch('serverAPI.Game')
    @patch('serverAPI.html')
    def test_check_game_state(self, mock_html, mock_game):
        mock_game.make_move.return_value = True
        mock_game.get_board.return_value = 'board'
        mock_html.generate_board.return_value = 'game board'
        result = self.app.get('/check_game/1/1/1')
        self.assertEqual(result, 'game board')
        self.assertEqual(response.status_code, 200)

    @patch('serverAPI.Game')
    def test_save_game_state(self, mock_game):
        mock_game.save_board.return_value = True
        result = self.app.post('/save_game/1')
        self.assertEqual(result, 'Game Saved')
        self.assertEqual(response.status_code, 200)

    @patch('serverAPI.Game')
    @patch('serverAPI.html')
    def test_load_game_state(self, mock_html, mock_game):
        mock_game.load_board.return_value = True
        mock_game.get_board.return_value = 'board'
        mock_html.generate_board.return_value = 'game board'
        result = self.app.get('/load_game/1')
        self.assertEqual(result, 'game board')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()