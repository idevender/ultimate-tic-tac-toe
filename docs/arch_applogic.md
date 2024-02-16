Using several states within a 2d matrix app logic will handle requests so that the game board can be properly updated, and/or a draw or winner chosen.
The States are as listed:
    PLAYABLE = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3
    A new game will have nine matrices filled with nine 0's for each spot on the tic-tac-toe board. Which will then get updated as the game goes on.
    
    When a player requests to make a move, that player id and position will determine the next state of the board.
    
    After each player makes a move the board state will be checked and will return the proper win/tie/none state.
