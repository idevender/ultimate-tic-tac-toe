import shelve


def setUp():
    """Creates the database for game states.

    Returns:
        int: the number of game states in the database.
    
        
    """
    with shelve.open('gameStates') as db:
        return len(db)


def save(name):
    """Saves a game state to the database.

    THIS IS A STUB

    Params:
        name (str): Assign a name to the newly stored game state.

    Raises:
        Standard IO errors if the game state cannot be saved properly.
    """
    pass


def load(name):
    """Loads a previously stored game state from the database.
    
    THIS IS A STUB

    Params:
        name (str): The name of the game state to be loaded.

    Raises:
        IOError: If the game state cannot be loaded properly.
    """
    pass


def remove(name):
    """Removes a previously stored game state from the database.

    THIS IS A STUB
    
    Params:
        name (str): The name of the game state to be removed.
    
    Raises:
        IOError: If the game state cannot be destroyed.
    """
    pass
