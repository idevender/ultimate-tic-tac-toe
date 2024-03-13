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



    def save_game(self, game_id):
        """Saves a game state to the database.

        THIS IS A STUB

        Parameters:
            game_id (str): Assign an identifier to the newly stored game state.

        Raises:
            IOError: If the game state cannot be saved properly.
        """
        pass


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

        THIS IS A STUB

        Parameters:
            name (str): The id of the game state to be removed.

        Raises:
            IOError: If the game state cannot be destroyed.
        """
        pass


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


    def save_user(self, username, password):
        """Saves a user to the database.

        Parameters:
            username (str): Save the user-created username.
            password (str): Save the user-created password.

        Raises:
            OSError: If the user cannot be saved properly.
        """
        with shelve.open(self.db_name) as db:
            if username in db:
                raise OSError(f"The user '{username}' is already taken, please choose another username.")

            db[username] = {
                'username': username,
                'password': password,
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

        THIS IS A STUB

        Parameters:
            username (str): The name of the user to be removed.

        Raises:
            IOError: If the user cannot be destroyed.
        """
        pass

