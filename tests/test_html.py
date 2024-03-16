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
from unittest import TestCase
from frontend import FrontEndOps, RenderEngine
import os


class TestFrontEndOps(TestCase):
    
    def setUp(self):
        self.test_frontend = FrontEndOps()

    def test_get_cell_coords_succ(self):
        test_cell_id = "57"
        expected_cell_coords = (5, 7)
        actual_coords = self.test_frontend.get_cell_coords(test_cell_id)
        self.assertEqual(actual_coords, expected_cell_coords)

    def test_get_cell_coords_error(self):
        cell_id = "C5" 
        with self.assertRaises(OSError):
            self.test_frontend.get_cell_coords(cell_id)

    def test_process_board_config(self):
        pass

    def test_update_board(self):
        pass

    def test_process_online_players(self, online_players):
        online_players = 123
        with self.assertRaises(TypeError):
            self.test_frontend.process_online_players(online_players=online_players)




class TestRenderEngine(TestCase):
    def setUp(self):
        self.test_render_engine = RenderEngine()

    def test_render_signup_page_exist(self):
        signup_page_path = os.path.join(os.path.dirname(__file__), "views/signup.tpl")
        self.assertTrue(os.path.exists(signup_page_path), "The sign up html template does not exist in the views folder!")

    def test_render_signup_page_form(self):
        test_signup_page = self.test_render_engine.render_signup_page()
        self.assertIn('<form', test_signup_page) 

    def test_render_login_page_exist(self):
        login_page_path = os.path.join(os.path.dirname(__file__), "views/login.tpl")
        self.assertTrue(os.path.exists(login_page_path), "The login html template does not exist in the views folder!")

    def test_render_login_page_form(self):
        test_login_page = self.test_render_engine.render_login_page()
        self.assertIn('<form', test_login_page) 

    def test_render_main_game_page_exist(self):
        main_page_path = os.path.join(os.path.dirname(__file__), "views/gamepage.tpl")
        self.assertTrue(os.path.exists(main_page_path), "The main game html template does not exist in the views folder!")

    def test_render_online_players_page_exist(self):
        online_players_page_path = os.path.join(os.path.dirname(__file__), "views/onlineplayers.tpl")
        self.assertTrue(os.path.exists(online_players_page_path), "The online players list html template does not exist in the views folder!")

    def test_render_updated_board(self, board_config):
        # check if the board_config is a 2d list
        if not isinstance(board_config, list):
            self.fail("The board_config is not a list!")
        
    
if __name__ == '__main__':
    unittest.main()
