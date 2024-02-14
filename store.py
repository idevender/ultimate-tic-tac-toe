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



    def save_game(self, name):
        """Saves a game state to the database.

        THIS IS A STUB

        Parameters:
            name (str): Assign a name to the newly stored game state.

        Raises:
            IOError: If the game state cannot be saved properly.
        """
        pass


    def load_game(self, name):
        """Loads a previously stored game state from the database.

        THIS IS A STUB

        Parameters:
            name (str): The name of the game state to be loaded.

        Raises:
            IOError: If the game state cannot be loaded properly.
        """
        pass


    def remove_game(self, name):
        """Removes a previously stored game state from the database.

        THIS IS A STUB

        Parameters:
            name (str): The name of the game state to be removed.

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


    def save_user(self, user_name):
        """Saves a user to the database.

        THIS IS A STUB

        Parameters:
            user_name (str): Assign a name to the newly stored user.

        Raises:
            IOError: If the user cannot be saved properly.
        """
        pass


    def load_user(self, user_name):
        """Loads a previously stored user from the database.

        THIS IS A STUB

        Parameters:
            user_name (str): The name of the user to be loaded.

        Raises:
            IOError: If the user state cannot be loaded properly.
        """
        pass


    def remove_user(self, user_name):
        """Removes a previously stored user from the database.

        THIS IS A STUB

        Parameters:
            user_name (str): The name of the user to be removed.

        Raises:
            IOError: If the user cannot be destroyed.
        """
        pass

