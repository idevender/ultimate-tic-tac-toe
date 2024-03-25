import shelve

class GameStateManager:
    """Class for managing game states using a shelve database."""

    
    def __init__(self, db_name='gameStates'):
        """
        Initializes the GameStateManager.

        Parameters:
            db_name (str): The name of the shelve database for game states.
        """
        self.db_name = db_name


    def setup_db(self):
        """Creates the database for game states.

        Returns:
            int: The number of game states in the database.
        """
        with shelve.open(self.db_name) as db:
            return len(db)

    def save_game(self, game_id="id", player1="player1", player2="player2", turn="player1", board=[[0 for _ in range(9)] for _ in range(9)]):
        """Saves a game state to the database.

        Parameters:
            game_id (str): Assign an identifier to the newly stored game state.

        Raises:
            IOError: If the game state cannot be saved properly.
        """

        with shelve.open(self.db_name) as db:
            if game_id in db:
                raise IOError(f"The game '{game_id}' already exists. Game not saved.")
            db[game_id] = {
                'gameID' : game_id,
                'player1': player1,
                'player2': player2,
                'board' : board,
                'turn' : turn
            }

    def load_game(self, game_id):
        """Loads a previously stored game state from the database.

        Parameters:
            game_id (str): The id of the game state to be loaded.

        Returns:
            game_state (dict): The game state information in a dictionary.

        Raises:
            IOError: If the game state cannot be loaded properly.
        """
        with shelve.open(self.db_name) as db:
            game_state = db.get(game_id)

            if game_state is None:
                raise IOError(f"The game '{game_id}' does not exist.")
            
            return game_state
        


    def remove_game(self, game_id):
        """Removes a previously stored game state from the database.
        
        Parameters:
            name (str): The id of the game state to be removed.

        Raises:
            IOError: If the game state cannot be destroyed.
        """
        with shelve.open(self.db_name) as db:
            game_state = db.get(game_id)

            if game_state is None:
                raise IOError(f"The game '{game_id}' does not exist.")
            
            del db[game_id]


class UserManager:
    """Class for managing user information using a shelve database."""

    def __init__(self, db_name='users'):
        """
        Initializes the UserInfoManager.

        Parameters:
            db_name (str): The name of the shelve database for user information.
        """
        self.db_name = db_name


    def setup_db(self):
        """Creates the database for user information.

        Returns:
            int: The number of users in the database.
        """
        with shelve.open(self.db_name) as db:
            return len(db)


    def save_user(self, username, password, online = False):
        """Saves a user to the database.

        Parameters:
            username (str): Save the user-created username.
            password (str): Save the user-created password.
            online (bool): Save the online status of the user.

        Raises:
            OSError: If the user cannot be saved properly.
        """
        with shelve.open(self.db_name) as db:
            if username in db:
                raise OSError(f"The user '{username}' is already taken, please choose another username.")

            db[username] = {
                'username': username,
                'password': password,
                'online': online
                }

    def load_user(self, username):
        """Loads a previously stored user from the database.

        Parameters:
            username (str): The name of the user to be loaded.

        Returns:
            user (dict): The user information in a dictionary.
        Raises:
            OSError: If the user state cannot be loaded properly.
        
        """
        with shelve.open(self.db_name) as db:
            user = db.get(username)
            if user is None:
                raise OSError(f"The user '{username}' does not exist.")
        return user


    def remove_user(self, username):
        """Removes a previously stored user from the database.

        Parameters:
            username (str): The name of the user to be removed.

        Raises:
            IOError: If the user cannot be destroyed.
        """
        with shelve.open(self.db_name) as db:
            user = db.get(username)

            if user is None:
                raise IOError(f"The user '{username}' does not exist.")
            
            del db[username]
    
    def set_user_online_status(self, username, status):
        """Sets the online status of a user in the database.

        Parameters:
            username (str): The name of the user to be updated.
            status (bool): The online status of the user.

        Raises:
            OSError: If the user status cannot be updated properly.
        """
        with shelve.open(self.db_name) as db:
            user = db.get(username)
            if user is None:
                raise OSError(f"The user '{username}' does not exist.")
            
            user['online'] = status

