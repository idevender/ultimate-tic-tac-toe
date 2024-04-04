import store
import hashlib
import uuid


class User:
    """Represents a user with a username and password.

    Attributes:
        username (str): A unique identifier for the user.
        password (str): The account password for the user.
    """

    def __init__(self, username, password):
        """Initializes a User object with a given username and password.

        Args:
            username (str): A unique identifier for the user.
            password (str): The account password for the user.
        """
        self.username = username
        self.password = password


class UserManager:
    """Manages user operations such as registration, login, and historical data.

    Attributes:
        user_db (store.UserManager): Instance of store.UserManager for database operations.
    """

    def __init__(self):
        """Initializes a UserManager object to manage user data."""
        self.user_db = store.UserManager()

    def setup(self):
        """Prepares the database for user data storage and retrieval.

        Returns:
            int: Number of users currently in the database.
        """
        return self.user_db.setup_db()

    def hash_password(self, password):
        """Hashes a password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Adds a new user to the system.

        Args:
            username (str): The chosen username for the new user.
            password (str): The chosen password for the new user.

        Returns:
            bool: True if the user was successfully registered, False otherwise.
        """
        # Check if the username already exists in the database
        with store.shelve.open(self.user_db.db_name) as db:
            if username in db:
                # Username already taken, return False to indicate failure
                return False

            # Hash the password
            hashed_password = self.hash_password(password)

            # Store the user with the hashed password
            db[username] = {'username': username,
                            'password': hashed_password, 'online': True}

        # Return True
        return True

    def login_user(self, username, input_password):
        """Authenticates a user's credentials and sets their status to online if successful.

        Args:
            username (str): The username to authenticate.
            input_password (str): The password provided by the user during login.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        with store.shelve.open(self.user_db.db_name, writeback=True) as db:
            user_data = db.get(username)
            if user_data and self.hash_password(input_password) == user_data['password']:
                user_data['online'] = True  # Set user as online
                db[username] = user_data  # Save the update
                return True
        return False

    def update_user_history(self, username, game_result):
        """Records the result of a user's game.

        Args:
            username (str): The username of the player.
            game_result (str): The outcome of the game ('win', 'loss', or 'draw').
        """
        pass

    def get_user_history(self, username):
        """Retrieves the game history for a user.

        Args:
            username (str): The username whose history is being requested.

        Returns:
            List[str]: The list of game outcomes for the user.
        """
        return []

    def get_user(self, username):
        """Retrieves a user by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The user object if found, None otherwise.
        """
        user_data = self.user_db.load_user(username)
        if user_data:
            return User(user_data['username'], user_data['password'])
        return None

    def update_user_password(self, username, new_password):
        """Updates the password for a specified user with a hashed password.

        Args:
            username (str): The username of the user.
            new_password (str): The new password for the user.

        Returns:
            bool: True if the password was successfully updated, False otherwise.
        """
        with store.shelve.open(self.user_db.db_name, writeback=True) as db:
            if username in db:
                # Hash the new password before updating
                hashed_new_password = self.hash_password(new_password)
                # Update the user's password with the hashed new password
                user_data = db[username]
                user_data['password'] = hashed_new_password
                # Ensuring the updated user data is saved back to the database
                db[username] = user_data
                return True  # Password update was successful
            else:
                # User does not exist in the database
                return False

    def get_all_online_users(self):
        """Retrieves all users from the database who are currently marked as online.

        Returns:
            list: A list of usernames of users who are online.
        """
        online_users = []
        with store.shelve.open(self.user_db.db_name) as db:
            for username, user_info in db.items():
                # Defaults to False if 'online' key is not there
                if user_info.get('online', False):
                    online_users.append(username)
        return online_users

    def gen_game_id(self, user_id1, user_id2):
        """Generates a unique game ID for a new game between two users and initializes the game.

        Args:
            user_id1 (str): The username of the first user.
            user_id2 (str): The username of the second user.

        Returns:
            str: A globally unique game ID.
        """
        # Generate a unique UUID for the new game
        unique_id = str(uuid.uuid4())

        # Initialize a new game with the generated ID, user1, and user2
        game_state_manager = store.GameStateManager(db_name='gameStates')
        game_state_manager.create_game(
            game_id=unique_id, player1=user_id1, player2=user_id2, turn=user_id1)

        return unique_id

    def get_leaderboard(self):
        """Retrieves the top 10 players sorted by their win counts from the user database.

        Returns:
            list: A list of tuples containing the username and win count of the top 10 players.
        """
        users_stats = []

        # Load all user data and collect wins
        with store.shelve.open(self.user_db.db_name) as db:
            for username, user_details in db.items():
                users_stats.append((username, user_details.get('wins', 0)))

        # Sort users by win counts in descending order
        leaderboard = sorted(users_stats, key=lambda x: x[1], reverse=True)

        # Return the top 10 players
        return leaderboard[:10]

    def get_active_games(self, username):
        """
        Retrieves a list of active games for a specified user without modifying store.py.

        Args:
            username (str): The username to fetch active games for.

        Returns:
            list: A list of lists, each containing [game_id, opponent_username] for active games.
        """
        active_games = []
        with store.shelve.open("data/gameStates.db") as db:
            for game_id, game_info in db.items():
                # Check if the game is active and if the user is a participant
                if game_info['winner'] is None and (game_info['player1'] == username or game_info['player2'] == username):
                    # Determine the opponent and append the game info to the list
                    opponent = game_info['player2'] if game_info['player1'] == username else game_info['player1']
                    active_games.append([game_id, opponent])

        return active_games
