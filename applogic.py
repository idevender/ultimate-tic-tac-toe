import store

class SuperTicTacToe:
    """
    A class to represent the Super Tic Tac Toe game.
    
    Attributes:
        board (list): A 9x9 list representing the game board.
        gameid (int): The ID of the game.
        playerTurn (int): The current player's turn.
        
    Methods:
        __init__(self)
        make_move(self, row, col)
        check_board_win(self)
        check_board_draw(self)
        check_game_win(self)
        check_game_draw(self)
        draw_fill(self)
        win_fill(self)
        load_board(self, gameid)
        save_board(self,gameid)
    """
    PLAYABLE = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3
        
    def create_game(self, gameid):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.playerTurn = SuperTicTacToe.PLAYER_ONE
        self.gameid = gameid
        self.save_board(gameid = self.gameid)

    def make_move(self, gameid, row, col):
        """
        Makes a move on the game board.

        Args:
            gameid (int): The ID of the game.
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            bool: True if the move resulted in a win or draw, False otherwise.
        """
        self.gameid = gameid
        self.load_board(self.gameid)

        if self.board[row][col] !=0:
            return False
        else:
            self.board[row][col] = self.playerTurn
            self.save_board(self.gameid)
            if(self.playerTurn == SuperTicTacToe.PLAYER_ONE):
                self.playerTurn = SuperTicTacToe.PLAYER_TWO
            else:
                self.playerTurn = SuperTicTacToe.PLAYER_ONE
    
    def check_states(self):
        if self.check_board_draw():
            self.check_game_draw()
            
        elif self.check_board_win():
            self.check_game_win()
    
    def check_board_draw(self):
        """
        Checks if the specific board is a draw.

        Returns:
            bool: True if the board is a draw, False otherwise.
        """
        for row in self.board:
            if 0 in row:
                return False
        return True
    
    def check_board_win(self):
        """
        Checks if a player has won the specific board.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] != 0:
                    return True
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] != 0:
                    return True
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] != 0:
                    return True
                if self.board[row+2][col] == self.board[row+1][col+1] == self.board[row][col+2] != 0:
                    return True
        return False
    
    def check_game_win(self):
        """
        Checks if a player has won the game.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if self.check_board_win(self.playerTurn, row, col):
                    return True
        return False
    
    def check_game_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.check_board_draw(row, col):
                    return False
        return True

    def draw_fill(self):
        """
        Fills the specific board with 3s to indicate a draw.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = SuperTicTacToe.DRAW

    def win_fill(self):
        """
        Fills the specific board with the player's number to indicate a win.
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = self.playerTurn
    
    def load_board(self, gameid):
        """
        Loads the game board and player turn from the game state manager.

        Args:
            gameid (int): The ID of the game.

        Returns:
            list: The loaded game board.
        """
        self.gameid = gameid
        self.board = store.GameStateManager.load_game(gameid)['board']
        self.playerTurn = store.GameStateManager.load_game(gameid)['turn']
        return self.board

       
    def save_board(self, gameid):
        """
        Saves the game board and player turn to the game state manager.

        Args:
            gameid (int): The ID of the game.
        """
        store.GameStateManager.save_game(gameid = gameid, turn = self.playerTurn, board = self.board)