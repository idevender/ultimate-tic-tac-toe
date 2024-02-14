# Store Architecture Overview
Created by: Evan Best

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

#### 1. `GameManager` Class
   - **Responsibilities:**
     - Manage game state storage and retrieval.
     - Handle the creation, updating, and removal of game states.
   - **Methods:**
     - `setup_db()`: Creates the database for game states.
     - `save_game_state(game_id, game_state)`: Saves a game state to the database.
     - `load_game_state(game_id)`: Loads a game state from the database.
     - `remove_game_state(game_id)`: Removes a game state from the database.

#### 2. `UserManager` Class
   - **Responsibilities:**
     - Manage user information storage and retrieval.
     - Handle the creation, updating, and removal of user information.
   - **Methods:**
     - `setup_db()`: Creates the database for user information.
     - `save_user(username, password)`: Saves a user to the database.
     - `load_user(username)`: Loads a user from the database.
     - `remove_user(username)`: Removes a user from the database.

