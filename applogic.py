from store import GameStateManager

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
    
    def create_game(self, gameid =1):
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
        self.subBoard = row

        if self.board[row][col] !=0:
            return False
        else:
            self.board[row][col] = self.playerTurn
            self.check_states()
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
            
    def fill(self, state):
        row = self.subBoard
        for j in range(9):
            self.board[row][j] = state
            break
    
    def check_board_draw(self):
        """
        Checks if the specific board is a draw.

        Returns:
            bool: True if the board is a draw, False otherwise.
        """
        row = self.subBoard
        for i in range(3):
            if self.board[row][0+(i*3)] == SuperTicTacToe.DRAW and self.board[row][1+(i*3)] == SuperTicTacToe.DRAW and self.board[row][2+(i*3)] == SuperTicTacToe.DRAW:
                self.fill(SuperTicTacToe.DRAW)
                return True
            if self.board[row][(3*i)] == SuperTicTacToe.DRAW and self.board[row][4] == SuperTicTacToe.DRAW and self.board[row][2+(i*3)] == SuperTicTacToe.DRAW:
                self.fill(SuperTicTacToe.DRAW)
                return True
            if self.board[row][0+i] == SuperTicTacToe.DRAW and self.board[row][3+i] == SuperTicTacToe.DRAW and self.board[row][6+i] == SuperTicTacToe.DRAW:
                self.fill(SuperTicTacToe.DRAW)
                return True
            
        
    def check_board_win(self):
        """
        Checks if a player has won the specific board.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        row = self.subBoard
        for i in range(3):
            if self.board[row][0+(i*3)] == self.playerTurn and self.board[row][1+(i*3)] == self.playerTurn and self.board[row][2+(i*3)] == self.playerTurn:
                self.fill(self.playerTurn)
                return True
            if self.board[row][(3*i)] == self.playerTurn and self.board[row][4] == self.playerTurn and self.board[row][2+(i*3)] == self.playerTurn:
                self.fill(self.playerTurn)
                return True
            if self.board[row][0+i] == self.playerTurn and self.board[row][3+i] == self.playerTurn and self.board[row][6+i] == self.playerTurn:
                self.fill(self.playerTurn)
                return True
    
    def check_game_win(self):
        """
        Checks if a player has won the game.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        if(self.check_board_win()):
            for i in range(3):
                if self.board[i*3] == self.board[1+(i*3)] and self.board[1+(i*3)]  == self.board[2+(i*3)]:
                    self.fill(self.playerTurn)
                    return True
                if self.board[(3*i)] == self.board[4] and self.board[4] == self.board[2+(i*3)]:
                    self.fill(self.playerTurn)
                    return True
                if self.board[0+i] == self.board[3+i] and self.board[3+i] == self.board[6+i]:
                    self.fill(self.playerTurn)
                    return True
 
    def check_game_draw(self, subboard):
        """
        Checks if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        if(self.check_board_draw()):
            for i in range(3):
                if self.board[i*3] == self.board[1+(i*3)] and self.board[1+(i*3)]  == self.board[2+(i*3)]:
                    self.fill(self.playerTurn)
                    return True
                if self.board[(3*i)] == self.board[4] and self.board[4] == self.board[2+(i*3)]:
                    self.fill(self.playerTurn)
                    return True
                if self.board[0+i] == self.board[3+i] and self.board[3+i] == self.board[6+i]:
                    self.fill(self.playerTurn)
                    return True
        
    def load_board(self, gameid):
        """
        Loads the game board and player turn from the game state manager.

        Args:
            gameid (int): The ID of the game.

        Returns:
            list: The loaded game board.
        """
        self.gameid = gameid
        self.board = GameStateManager.load_game(gameid).get('board')
        self.playerTurn = GameStateManager.load_game(gameid).get('turn')
        return self.board

       
    def save_board(self, gameid):
        """
        Saves the game board and player turn to the game state manager.

        Args:
            gameid (int): The ID of the game.
        """
        GameStateManager.save_game(gameid = gameid, turn = self.playerTurn, board = self.board)
