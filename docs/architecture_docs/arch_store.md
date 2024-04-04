# Store Architecture Overview
Created by: Evan Best

## Imports
The following modules are imported:
- `shelve`: For persistence storage of game states and user information.

## Components
#### 1. `gameStates` Database
   - **Purpose:** Store game states for each ongoing game.
   - **Implementation:** Uses the `shelve` module for a simple key-value store.
   - **Key:** Game ID (a unique identifier for each game).
   - **Value:** A game state object.

#### 2. `users` Database
   - **Purpose:** Store user information, including usernames and hashed passwords.
   - **Implementation:** Uses the `shelve` module for a simple key-value store.
   - **Key:** Username or email.
   - **Value:** Dictionary containing user information.

## Classes

#### 1. `GameStateManager` Class
   - **Responsibilities:**
     - Manage game state storage and retrieval.
     - Handle the creation, updating, and removal of game states.
   - **Methods:**
     - `setup_db()`: Creates the database for game states.
     - `create_game(game_id, player1, player2, turn, board, winner)` - Creates a new game and saves to the database.
     - `save_game(game_id, board, winner, turn)`: Saves changes made to a game state to the database.
     - `load_game(game_id)`: Loads a game state from the database.
     - `remove_game(game_id)`: Removes a game state from the database.

#### 2. `UserManager` Class
   - **Responsibilities:**
     - Manage user information storage and retrieval.
     - Handle the creation, updating, and removal of user information.
   - **Methods:**
     - `setup_db()`: Creates the database for user information.
     - `create_user(username, password, online, wins, losses, draws)`: Creates a new user and saves to the database.
     - `save_user(username, wins, losses, draws)`: Saves changes made to a user to the database.
     - `load_user(username)`: Loads a user from the database.
     - `remove_user(username)`: Removes a user from the database.
     - `set_user_online_status(username, status)`: Updates the online status of a user.

