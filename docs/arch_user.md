# User Architecture Documentation
**Created by:** Devender Singh

## Components:
### User Database
- **Purpose:** Holds user details, including usernames and hashed passwords.
- **Implementation:** Utilizes a dictionary for basic key-value storage.
- **Key:** Username
- **Value:** User object containing user data.

## Classes:
### User Class
- **Responsibilities:**
  - Represents a user with a username and password.
- **Methods:**
  - `__init__(username, password)`: Initializes a User instance with given attributes.
- **Attributes:**
  - `username`: Unique identifier for the user.
  - `password`: Account password.

### UserManager Class
- **Responsibilities:**
  - Manages user tasks such as registration, login, and tracking historical data.
- **Methods:**
  - `setup()`: Prepares the database for user data management.
  - `register_user(username, password)`: Adds a new user to the system.
  - `login_user(username, password)`: Authenticates user credentials.
  - `update_user_history(username, game_result)`: Records a user's game outcome.
  - `get_user_history(username)`: Retrieves game history for a user.
  - `log_out_user(username)`: Terminates the session for the specified user.
  - `get_user(username)`: Retrieves a user object by username.
  - `update_user_password(username, new_password)`: Updates the password for a specified user.

## Implementation Details:
- **User Registration:** The `register_user` method creates a new user instance with provided credentials and stores it in the user database.
- **User Authentication:** The `login_user` method verifies the provided username and password, returning True if they match.
- **User History:** The `update_user_history` method logs a user's game result for historical tracking.
- **Session Management:** The `log_out_user` method ends the session for a specific user.

### User UML Diagram

![User UML Diagram](./diagrams/User_UML_diagram.png)

