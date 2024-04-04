
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
    

    def get_cell_coords(self):
        """
        Returns the coordinates of the button/cell clicked by a player on the game board in the app.
     
        Returns:
            int, int: x coordinate, y coordinate of the cell clicked 
        
        """

        # Getting the cell Coordinates from the request
        cell_coords = request.forms.get('coordinate')

        # Seperating the X and Y Coordinates from the cell ID String
        cell_coords = cell_coords.split(',') 


        cell_x_coord = int(cell_coords[0]) # Grid Cell X Coordinate
        cell_y_coord = int(cell_coords[1]) # Grid Cell Y Coordinate

        return cell_x_coord, cell_y_coord
    

    def update_board(self, game_board, turn, current_user, opponent, game_id):
        """
        Updates the game board on the front end.

        Args:
            board (2d list): A 9x9 list representing the game board.
        
        Returns:
            str: The updated game board on the front end.
        """

        # Making sure the game_board is well recieved
        if not game_board:
            return "Game Board Not Found"
        if not isinstance(game_board, list):
            raise TypeError("The game board is not a list.")
        
    
        # Making sure the turn is well recieved on the frontend
        if turn == 1:
            turn = "It's your turn"
        elif turn == 2:
            turn = f"It's {opponent}'s turn"

        converted_board = [] # A list to store the converted board

        # Converting the game board to the frontend format according to the board received
        for row in game_board:
            converted_row = []
            for col in row:
                if col == 0:
                    converted_row.append(" ")
                elif col == 1:
                    converted_row.append("X")
                elif col == 2:
                    converted_row.append("O")
            converted_board.append(converted_row)

        return self.AppRenderEngine.render_updated_board(converted_board, turn, current_user, opponent, game_id)


    def process_online_players(self, online_players, current_player, leaderboard_list, current_wins, current_losses):
        """
        Gets the list of online players from the server.
        
        Args:
            online_players (list): A list of online players.
            current_player (str): The current player.
            leaderboard_list (list): A list of leaderboard entries.
            current_wins (int): The number of wins of the current player.
            current_losses (int): The number of losses of the current player.

        Throws:
            TypeError: If the online players list is not a list.
            TypeError: If the online players list contains non-string elements.
            TypeError: If the leaderboard list is not a list.
            TypeError: If the current wins and losses are not integers.

        Returns:
            self.AppRenderEngine.render_online_players (str): The template for the online player list page.
        """

        if not isinstance(online_players, list) and not isinstance(current_player, str):
            raise TypeError("The online players list is not a list.")
        if not all(isinstance(player, str) for player in online_players):
            raise TypeError("The online players list contains non-string elements.")
        if not isinstance(leaderboard_list, list):
            raise TypeError("The leaderboard list is not a list.")
        if not isinstance(current_wins, int) and not isinstance(current_losses, int):
            raise TypeError("The current wins and losses are not integers.")


        current_player_rank = 0 # Variable to store the rank of the current player

        # Looping through the leaderboard list to get the rank of the current player
        for i in range(len(leaderboard_list)):
            if leaderboard_list[i][0] == current_player:
                current_player_rank = leaderboard_list[i][1]

        return self.AppRenderEngine.render_online_players(online_players, current_player, leaderboard_list, current_player_rank, current_wins, current_losses)


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

        self.signup_page = template('signup.html')
        self.login_page = template('login.html')
        self.reset_password = template('resetpassword.html')

    def render_signup_page(self):
        """
        Renders the signup page of the game app.

        Returns:
           signup_page (str): The template for the sign up page.

        OSError:
            If the template file cannot be found.
        """
        
        if not self.signup_page:
            raise OSError("The sign up template file cannot be found.")

        return self.signup_page


    def render_login_page(self):
        """
        Renders the login page of the game app.

        Returns:
            login_page (str): The template for the login page.
        
        OSError:
            If the template file cannot be found.
        """

        if not self.login_page:
            raise OSError("The login template file cannot be found.")
        
        return self.login_page


    def render_reset_password(self):
        """
        Renders the reset password page of the game app.

        Returns:
            reset_password (str): The template for the reset password page.

        OSError:
            If the template file cannot be found.
        """

        if not self.reset_password:
            raise OSError("The reset password template file cannot be found.")

        return self.reset_password


    def render_updated_board(self, board_config, turn, current_user, opponent, game_id):
        """
        Updates the game board on the main game page of the game app.

        Args:
            board_config (2d list): A 9x9 list representing the game board.
        """

        return template('gamepage.html', board_config=board_config, turn=turn, current_user = current_user, opponent=opponent, game_id=game_id)


    def render_online_players(self, online_players, current_player, leaderboard_list,current_player_rank, curr_wins, curr_losses):
        """
        Renders the online players page of the game app.    
        """

        return template('onlineplayers.html', online_players=online_players, current_player=current_player, leaderboard_list=leaderboard_list, current_player_rank=current_player_rank, curr_wins=curr_wins, curr_losses=curr_losses)