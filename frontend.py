
# Importing the required libaries
from bottle import template, request
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

        # Make sure the game_board is well recieved
        if not game_board:
            return "Game Board Not Found"
        if not isinstance(game_board, list):
            raise TypeError("The game board is not a list.")


        return self.AppRenderEngine.render_updated_board(game_board)
    

    def get_cell_coords(self):
        """
        Returns the coordinates of the button/cell clicked by a player on the game board in the app.
     
        Returns:
            int, int: x coordinate, y coordinate of the cell clicked 
        
        """

        # Getting the cell Coordinates from the request
        cell_coords = request.forms.get('cordinate')

        # Seperating the X and Y Coordinates from the cell ID String
        cell_coords = cell_coords.split(',') 


        cell_x_coord = int(cell_coords[0]) # Grid Cell X Coordinate
        cell_y_coord = int(cell_coords[1]) # Grid Cell Y Coordinate

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


    def process_online_players(self, online_players):
        """
        Gets the list of online players from the server.
        
        Args:
            online_players (list): A list of online players.

        Returns:
            self.AppRenderEngine.online_players_page (str): The template for the online player list page.
        """

        if not isinstance(online_players, list):
            raise TypeError("The online players list is not a list.")
        if not all(isinstance(player, str) for player in online_players):
            raise TypeError("The online players list contains non-string elements.")

        return self.AppRenderEngine.render_online_players(online_players)


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

        self.signup_page = template('signup')
        self.login_page = template('login')
        self.main_game_page = template('gamepage')
        #self.online_players_page = template('onlineplayers')


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


    def render_online_players(self, online_players):
        """
        Renders the online players page of the game app.    
        """

        return template('online_players', online_players=online_players)