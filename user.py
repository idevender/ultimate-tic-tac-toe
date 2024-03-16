import store
import hashlib

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
        """
        self.user_db.save_user(username, password)

    def login_user(self, username, password):
        """Authenticates a user's credentials.

        Args:
            username (str): The username to authenticate.
            password (str): The password to authenticate.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        user = self.user_db.load_user(username)
        return user and user['password'] == password

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

    def log_out_user(self, username):
        """Ends the session for the specified user.

        Args:
            username (str): The username of the user to log out.
        """
        pass

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
                db[username] = user_data  # Ensuring the updated user data is saved back to the database
                return True  # Password update was successful
            else:
                # User does not exist in the database
                return False

    def get_all_users(self):
        """Retrieves all users from the database and returns them as a list of usernames.

        Returns:
            list: A list of usernames representing all the users.
        """
        all_usernames = []
        with store.shelve.open(self.user_db.db_name) as db:
            all_usernames.extend(db.keys())
        return all_usernames
