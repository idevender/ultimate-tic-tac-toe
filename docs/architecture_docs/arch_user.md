# User Architecture Documentation
**Created by:** Devender Singh

## Introduction
This document outlines the architecture and design of the User Management System for our application, focusing on user operations such as registration, authentication, password management, and activity tracking.

## Components:
### User Database
- **Purpose:** HoSecurely stores user details, including usernames and hashed passwords, ensuring confidentiality and integrity..
- **Implementation:** Employs shelve for persistent storage, providing an efficient and straightforward mechanism for data access and manipulation.

### Security Module
- **Purpose:** Handles the secure hashing of user passwords, enhancing the security of stored credentials.
- **Implementation:** Utilizes the hashlib module to implement SHA-256 hashing, ensuring robust and secure password storage.

### Unique Identifier Generator
- **Purpose:** Generates unique identifiers for game sessions, facilitating the management and differentiation of user activities.
- **Implementation:** Leverages the uuid module to produce unique game IDs, ensuring the uniqueness and non-replicability of session identifiers.

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
  - `setup()`: Initializes the user database for storage and retrieval.
  - `hash_password(password)`: Generates a SHA-256 hash of the user's password.
  - `register_user(username, password)`: Registers a new user with hashed password storage.
  - `login_user(username, input_password)`: Authenticates a user based on hashed password comparison.
  - `update_user_password(username, new_password)`: Securely updates a user's password with hashing.
  - `get_all_users()`: Retrieves all user names from the database.
  - `gen_game_id(user_id1, user_id2)`: Generates and initializes a unique game ID for a session between two users.


## Implementation Details

### User Registration
- The `register_user` method adds a new user to the system with a hashed password, enhancing security by preventing the storage of plain text passwords. It checks if the username already exists in the database and, if not, stores the user with a SHA-256 hashed password. This method returns a boolean indicating the success or failure of the user registration process.

### User Authentication
- The `login_user` method authenticates a user's credentials by hashing the input password and comparing it with the stored hashed password in the database. This process ensures that user authentication is performed securely without exposing or comparing plain text passwords. It returns `True` if the authentication is successful, otherwise `False`.

### Password Management
- The `update_user_password` method allows users to securely update their passwords. It hashes the new password before updating the stored password in the database. This method ensures that users' new passwords are stored securely and not in plain text, enhancing the overall security of the user management system.

### User History and Session Management
- The `update_user_history` method records the outcomes of a user's games, allowing for historical tracking of game results.
- The `log_out_user` method terminates a user's session, effectively logging them out of the system. This function is crucial for maintaining the security and integrity of user sessions.

### Game Session Initialization
- The `gen_game_id` method generates a unique game ID for a new game session between two users and initializes the game state in the database. This method uses a UUID to ensure that each game session has a unique identifier, facilitating the management of individual game sessions. The initialization of the game state includes setting the player details and the initial game board, ensuring that the game is ready to be played immediately upon creation.


## Key Functionalities

### Secure User Registration and Authentication
- Employs SHA-256 hashing for password security during registration and authentication processes.

### Game Session Management
- Innovatively generates unique game IDs for sessions and initializes these in the database, ensuring effective game management.

### Password Security
- Facilitates secure password updates by hashing new passwords prior to storage, enhancing overall security.

## Future Directions

### Enhanced Security Measures
- Implementing additional layers of security, such as two-factor authentication, to further safeguard user data.

### User Activity Analytics
- Extending the system to capture and analyze user activity patterns for improved user engagement and system optimization.

![UML Diagram for User](../diagrams/User_UML_diagram.png)
