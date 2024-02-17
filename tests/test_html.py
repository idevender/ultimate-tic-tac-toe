
from unittest import TestCase
from ..html import FrontEndOps, RenderEngine
import os


class TestFrontEndOps(TestCase):
    
    def setUp(self):
        myDisplay = FrontEndOps()
        pathFinder = os.path.dirname(os.path.abspath(__file__))

    def test_get_cell_coords_succ(self):
        pass

    def test_get_cell_coords_error(self):
        pass

    def test_update_board_succ(self):
        pass

    def test_update_board_error(self):
        pass



class TestRenderEngine(TestCase):
    def setUp(self):
        render_tester = RenderEngine()
        pathFinder = os.path.dirname(os.path.abspath(__file__))

    
    def test_render_signup_page_succ(self):
        pass

    def test_render_signup_page_error(self):
        pass

    def test_render_login_page_succ(self):
        pass

    def test_render_login_page_error(self):
        pass

    def test_render_main_game_page(self):
        pass

    def test_render_updated_board(self):
        pass