class SuperTicTacToe:
    """
    A class to represent the Super Tic Tac Toe game.
    
    Attributes:
        board (list): A 9x9 list representing the game board.
        
    Methods:
        __init__(self)
        make_move(self, row, col)
        check_board_win(self, player)
        check_board_draw(self)
        check_game_win(self, player)
        check_game_draw(self)
        draw_fill(self)
        win_fill(self, player)
    """
    PLAYABLE = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3
    
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
    
    def make_move(self, row, col, player):
        """
        Makes a move on the game board.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            player (int): The player making the move.

        Returns:
            bool: True if the move resulted in a win or draw, False otherwise.
        """
        
        if(self.board[row][col] == 0):
            self.board[row][col] = player
        pass
    
    def check_board_draw(self):
        """
        Checks if the specific board is a draw.

        Returns:
            bool: True if the board is a draw, False otherwise.
        """
        pass
    
    def check_board_win(self):
        """
        Checks if a player has won the specific board.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        pass
        
    def check_game_win(self):
        """
        Checks if a player has won the game.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        pass
    
    def check_game_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        pass
    
    def draw_fill(self):
        """
        Fills the specific board with 3s to indicate a draw.
        """
        pass
    
    def win_fill(self, player):
        """
        Fills the specific board with the player's number to indicate a win.
        
        Args:
            player (int): The player number.
        """
        pass 
    
    def get_board(self):
            """
            Returns the current state of the board.

            Returns:
                list: The current state of the board.
            """
            return self.board
