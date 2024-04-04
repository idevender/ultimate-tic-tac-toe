from store import GameStateManager

class SuperTicTacToe:
    """
    A class to represent the Super Tic Tac Toe game.
    
    Attributes:
        board (list): A 9x9 list representing the game board.
        gameid (int): The ID of the game.
        playerTurn (int): The current player's turn.
    """
    PLAYABLE = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3
    
    def create_game(self, gameid):
        """
        Creates a new game with the given ID.
        
        Args:
            gameid (int): The ID of the game.
        """
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.playerTurn = SuperTicTacToe.PLAYER_ONE
        self.gameid = gameid
        self.winner = None
        self.save_board()

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
        self.load_board(gameid)
        self.subBoard = row
        self.endGame = False
        self.winner = None
        
        if self.board[row][col] != 0:
            return False
        else:
            self.board[row][col] = self.playerTurn
            self.check_states()
            if self.playerTurn == SuperTicTacToe.PLAYER_ONE:
                self.playerTurn = SuperTicTacToe.PLAYER_TWO
            else:
                self.playerTurn = SuperTicTacToe.PLAYER_ONE
            self.save_board()
            self.game_over()
            return True, self.board, self.playerTurn
    
    def check_states(self):
        """
        Checks the states of the board and the game.
        """
        if self.check_board_win():
            self.fill(self.playerTurn)
            if self.check_game_win():
                self.fillGame(self.playerTurn)
                self.winner = self.playerTurn
        elif self.check_board_draw():
            self.fill(SuperTicTacToe.DRAW)
            if self.check_game_draw():
                self.fillGame(SuperTicTacToe.DRAW)
                self.winner = SuperTicTacToe.DRAW
            
    def fill(self, state):
        """
        Fills the current sub-board with the given state.

        Args:
            state (int): The state to fill the sub-board with.
        """
        row = self.subBoard
        for j in range(9):
            self.board[row][j] = state
        
    def fillGame(self, state):
        """
        Fills the entire game board with the given state.

        Args:
            state (int): The state to fill the game board with.
        """
        for i in range(9):
            for j in range(9):
                self.board[i][j] = state                
    
    def check_board_draw(self):
        """
        Checks if the specific board is a draw.

        Returns:
            bool: True if the board is a draw, False otherwise.
        """
        row = self.subBoard
        counter = self.board[row].count(0)
        if counter == 0:
            return True
        return False
                
    def check_board_win(self):
        """
        Checks if a player has won the specific board.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        row = self.subBoard
        for i in range(3):
            if self.board[row][0+(i*3)] == self.playerTurn and self.board[row][1+(i*3)] == self.playerTurn and self.board[row][2+(i*3)] == self.playerTurn:
                return True
            if self.board[row][(3*i)] == self.playerTurn and self.board[row][4] == self.playerTurn and self.board[row][8-(i*3)] == self.playerTurn:
                return True
            if self.board[row][0+i] == self.playerTurn and self.board[row][3+i] == self.playerTurn and self.board[row][6+i] == self.playerTurn:
                return True
        return False
    
    def check_game_win(self):
        """
        Checks if a player has won the game.

        Returns:
            bool: True if a player has won, False otherwise.
        """
        win = [self.playerTurn] * 9
        
        for i in range(3):
            if self.board[i*3] == win and self.board[1+(i*3)] == win and self.board[1+(i*3)]  == win:
                return True
            if self.board[(3*i)] == win and self.board[4] == win and self.board[2+(i*3)] == win:
                return True
            if self.board[0+i] == win and self.board[3+i] == win and self.board[6+i] == win:
                return True
        return False
 
    def check_game_draw(self):
        """
        Checks if the game is a draw.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        draw = [SuperTicTacToe.DRAW] * 9
        
        counter = self.board.count(draw)
        if counter >= 7:
            return True
        return False       
    
    def load_board(self, gameid):
        """
        Loads the game board and player turn from the game state manager.

        Args:
            gameid (int): The ID of the game.

        Returns:
            list: The loaded game board.
        """
        self.gameid = gameid
        game = GameStateManager().load_game(gameid)
        self.board = game.get('board')
        self.playerTurn = game.get('turn')
        self.winner = None
        return self.board, self.playerTurn
       
    def save_board(self):
        """
        Saves the game board and player turn to the game state manager.
        """
        GameStateManager().save_game(game_id=self.gameid, turn=self.playerTurn, board=self.board, winner=self.winner)
        
    def game_over(self):
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        if self.winner != None:
            GameStateManager().remove_game(self.gameid)
       
