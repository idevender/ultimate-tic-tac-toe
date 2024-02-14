import shelve


# GAME STATE METHODS

def setup_game_db():
    """Creates the database for game states.

    Returns:
        int: the number of game states in the database.
    
        
    """
    with shelve.open('gameStates') as db:
        return len(db)


def save_game(name):
    """Saves a game state to the database.

    THIS IS A STUB

    Params:
        name (str): Assign a name to the newly stored game state.

    Raises:
        Standard IO errors if the game state cannot be saved properly.
    """
    pass


def load_game(name):
    """Loads a previously stored game state from the database.
    
    THIS IS A STUB

    Params:
        name (str): The name of the game state to be loaded.

    Raises:
        IOError: If the game state cannot be loaded properly.
    """
    pass


def remove_game(name):
    """Removes a previously stored game state from the database.

    THIS IS A STUB

    Params:
        name (str): The name of the game state to be removed.
    
    Raises:
        IOError: If the game state cannot be destroyed.
    """
    pass


# USER INFORMATION METHODS

def setup_user_db():
    """Creates the database for user information.

    Returns:
        int: the number of users in the database.
    
        
    """
    with shelve.open('users') as db:
        return len(db)
    
def save_user(user_name):
    """Saves a user to the database.

    THIS IS A STUB

    Params:
        user_name (str): Assign a name to the newly stored user.

    Raises:
        Standard IO errors if the user cannot be saved properly.
    """
    pass


def load_user(user_name):
    """Loads a previously stored user from the database.
    
    THIS IS A STUB

    Params:
        user_name (str): The name of the user to be loaded.

    Raises:
        IOError: If the user state cannot be loaded properly.
    """
    pass


def remove_user(user_name):
    """Removes a previously stored user from the database.

    THIS IS A STUB

    Params:
        user_name (str): The name of the user to be removed.
    
    Raises:
        IOError: If the user cannot be destroyed.
    """
    pass

