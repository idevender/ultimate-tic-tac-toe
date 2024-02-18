
# Importing the required libaries
from bottle import template
import os


class FrontEndOps:
    """
    Class that handles all the operations related to the front end of the super tic tac toe web app.
    """
    
    def __init__(self):
        """
        Initializes the front end operations of the super tic tac toe web app.

        Attr:
            AppRenderEngine (RenderEngine): An instance of the render engine class.
        """

        self.AppRenderEngine = RenderEngine()

    
    def process_board_config(self, game_board):
        """
        Processes the game board configuration recieved from the backend.

        Args:
        game_board (2d list): A 9x9 list representing the game board.
        """

        pass
    

    def get_cell_coords(self, cell_id):
        """
        Returns the coordinates of the button/cell clicked by a player on the game board in the app.

        Args:
            cell_id (str): The id of the button/cell clicked by a player on the game board.
        
        Returns:
            int, int: x coordinate, y coordinate of the cell clicked 
        
        """

        cell_x_coord = int(cell_id[0])    
        cell_y_coord = int(cell_id[1])

        return cell_x_coord, cell_y_coord
    

    def update_board(self, game_board):
        """
        Updates the game board on the front end.

        Args:
            board (2d list): A 9x9 list representing the game board.
        
        Returns:
            str: The updated game board on the front end.
        """

        return self.AppRenderEngine.render_updated_board(game_board)



# Class that handles the rendering of all the html templates for the super tic tac toe app
class RenderEngine:
    """
    Class that handles the rendering of the html templates for the super tic tac toe web app.
    """

    def __init__(self):
        """
        Initializes the render engine for the super tic tac toe web app.

        Attributes:
            signup_page (str): The template for the sign up page.
            login_page (str): The template for the login page.
            main_game_page (str): The template for the main game page.
        """

        self.signup_page = template('signup_page')
        self.login_page = template('login_page')
        self.main_game_page = template('main_game_page')


    def render_signup_page(self):
        """
        Renders the signup page of the game app.

        Returns:
           signup_page (str): The template for the sign up page.

        OSError:
            If the template file cannot be found.
        """
        
        return self.signup_page


    def render_login_page(self):
        """
        Renders the login page of the game app.

        Returns:
            login_page (str): The template for the login page.
        
        OSError:
            If the template file cannot be found.
        """
        
        return self.login_page


    def render_main_game_page(self, board_config):
        """
        Renders the main game page of the game app.

        Returns:
            main_game_page (str): The template for the main game page.
        
        OSError:
            If the template file cannot be found.
        """
        
        return self.main_game_page


    def render_updated_board(self, board_config):
        """
        Updates the game board on the main game page of the game app.

        Args:
            board_config (2d list): A 9x9 list representing the game board.
        """

        return template('main_game_page', board_config=board_config)

