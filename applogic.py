class SuperTicTacToe:
    PLAYABLE = 0
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    TIED = 3
    
    
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.current_player = 1  # Start with player 1
    
    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            if self.check_win(self.current_player):
                print(f"Player {self.current_player} wins!")
                return True
            if self.check_draw():
                print("The game is a draw!")
                self.fill_board_with_3()  # Fill the board with 3s to indicate a draw
                return True
            self.current_player = PLAYER_ONE if self.current_player == PLAYER_TWO else 2
        else:
            print("This cell is already taken. Choose another one.")
        return False
    
    def check_win(self, player):
        for i in range(9):
            if all(cell == player for cell in self.board[i]) or all(self.board[j][i] == player for j in range(9)):
                return True
        if all(self.board[i][i] == player for i in range(9)) or all(self.board[i][8-i] == player for i in range(9)):
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            if 0 in row:
                return False
        return True
    
    def fill_board_with_3(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = 3

    def play(self, row, col, player):
        if(self.board[row][col] == 0):
            self.board[row][col] = player
