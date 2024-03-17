# AppLogic documentation (SuperTicTacToe class) 
**Created by Cameron Selci**

## Class Constants (Board States) & Details:

The app logic uses several states within a 2D matrix to handle requests for updating the game board and determining if there is a draw or a winner. The states are as follows:

- **PLAYABLE**: Represents a state that can be played upon. Represented by 0.
- **PLAYER_ONE**: Represents one of the players and can be played on the playable state. Represented by 1.
- **PLAYER_TWO**: Represents one of the players and can be played on the playable state. Represented by 2.
- **DRAW**: Represents a state that can't be played upon. Sub-boards will be filled with either DRAW or PLAYER states when completed with a tie or win. Represented by 3.

- A new game starts with 9x9 matrix filled with nine 0's, representing each spot on the tic-tac-toe board. 
- Each sub-board(3x3 list) is updated as the game progresses. 
- When a player requests to make a move, their player ID and position determines the next state of the board. After each player makes a move, the board state is checked, and the appropriate game/board state is returned.

## Attributes:

- `board`: A two-dimensional matrix that represents the game state. Rows are initialized with 0's, representing a playable state.
- `playerTurn`: Keeps track of player turn.
- `gameid`: gameid for specific board.

## Methods:

- `create_board`: Creates new board.
- `make_move`: Updates the board with the player's move.
- `check_board_win`: Determines if a win condition is met on any sub-board.
- `check_board_draw`: Determines if the current sub-board is a draw.
- `check_game_win`: Checks if there's an overall win across the entire game board.
- `check_game_draw`: Verifies if the game has ended in a draw.
- `draw_fill`: Marks a sub-board as a draw, if applicable.
- `win_fill`: Marks a sub-board as a player win for specified player.
- `load_board`: Load board from store and returns using gameid.
- `save_board`: Save board using gameid.