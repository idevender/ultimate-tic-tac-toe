# SuperTicTacToe Game Architecture Document

## Overview
The SuperTicTacToe class represents an enhanced version of the classic Tic Tac Toe game, featuring a 9x9 game board. This document outlines the architecture, design principles, and interaction flow of the SuperTicTacToe game, focusing on its implementation, external dependencies, and interaction with the GameStateManager.

## System Architecture
### Components
- SuperTicTacToe Class: Manages the game logic, player interactions, and the state of the game board.
- GameStateManager (External Dependency): Handles persistence, including saving, loading, and deleting game states to and from a data store.

### Data Flow
1. `Game Initialization:` A new game is created with a unique game ID, initializing the 9x9 game board and setting the current player.
2. `Making Moves:` Players make moves by specifying the desired row and column on the board. The game logic determines the validity of the move, updates the board, and toggles the player turn.
3. `Checking Game State:` After each move, the game state is evaluated to determine if there is a win, draw, or if the game continues.
4. `Saving and Loading Game State:` The current state of the game is periodically saved to a data store via the GameStateManager. This state can be retrieved to continue the game.
5. `Game Conclusion:` Once a win or draw is detected, the game concludes. The final state can be saved, and then the game data is removed from the data store.


## Implementation Details
### Game Logic
The game logic includes methods for making moves, checking for a win or draw, and switching turns between two players.
The board is a 9x9 matrix where each cell can be in one of four states: playable, occupied by player one, occupied by player two, or part of a draw.

### State Management
The GameStateManager is used for persisting game state information, including the current state of the board, the player's turn, and the game winner.
Methods save_board and load_board interact with the GameStateManager to maintain game continuity and enable game sessions to be paused and resumed.

### Error Handling and Validation
The system includes checks to validate moves, ensuring they are made in playable spaces and within the board's bounds.
It handles errors gracefully, such as attempting to load a non-existent game or making an invalid move.

### Interaction with External Systems
The SuperTicTacToe class depends on the GameStateManager for all operations related to the persistence of game state. This separation of concerns allows for modularity and easier maintenance or replacement of the storage mechanism.

## Methods:

- `create_board`: Creates new board and saves it.
- `make_move`: Updates the board with the player's move. Triggers each method so that the game updates properly every move.
- `check_board_win`: Determines if a win condition is met on any sub-board. Triggers the subboard to fill with player number. Then checks game win.
- `check_board_draw`: Determines if the current sub-board is a draw. Checks draw if no win and fills subboard with draw number. Then checks game Draw.
- `check_game_win`: Checks if there's an overall win across the entire game board. Checks overall game win using logic and then fills entire game with playernumber win.
- `check_game_draw`: Verifies if the game has ended in a draw. Same as win fill, but with draw and draw number.
- `fill`: Filling subboards.
- `fill_game`: For filling games after game win check being true.
- `load_board`: Load board from store using gameid.
- `save_board`: Save board using gameid, winner, board, and playerTurn.