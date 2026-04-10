"""
Chess Board Module

This module defines the core Board class used to represent and manage the state of a chess game.

The Board class is responsible for:
- Initialising the chess board in the standard starting position
- Storing the current state of the game using a 2D list representation
- Handling basic piece movement between squares

Board Representation:
- The board is an 8x8 grid (list of lists)
- Each element represents a square on the board
- Uppercase letters represent White pieces (P, R, N, B, Q, K)
- Lowercase letters represent Black pieces (p, r, n, b, q, k)
- A dot "." represents an empty square

Coordinate System:
- The board uses [row][column] indexing
- Row 0 is the top of the board (Black side)
- Row 7 is the bottom of the board (White side)

Note:
This module does not handle any graphical rendering or user input.
It is purely responsible for game state and logic. The GUI layer interacts
with this class to display the board and apply moves.
"""

class Board:
    def __init__(self):
        self.board = self.create_starting_board()
        self.turn = "white"

    def create_starting_board(self):              
        return [
            ["r","n","b","q","k","b","n","r"],
            ["p","p","p","p","p","p","p","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            ["P","P","P","P","P","P","P","P"],
            ["R","N","B","Q","K","B","N","R"]
        ]
    
    def get_piece(self, row, col):
        return self.board[row][col]

    
    def move_piece(self, start, end):
        if not self.is_legal_move(start, end):
            return

        sr, sc = start             # define the starting and ending sqaures using the row and column
        er, ec = end

        piece = self.board[sr][sc] # access the piece in the selected square
        self.board[sr][sc] = "."   # replace the starting square with an empty square
        self.board[er][ec] = piece # place the selected piece in the chosen square

        self.turn = "black" if self.turn == "white" else "white"

    def get_piece_colour(self, piece):
        if piece == ".":
            return None
        return "white" if piece.isupper() else "black"
    
    def is_legal_move(self, start, end):
        sr, sc = start
        er, ec = end

        piece = self.board[sr][sc]
        target = self.board[er][ec]

        if piece == ".": # can't move an empty square
            return None
        
        if self.get_piece_colour(piece) != self.turn: # must move your own turn
            return False
        
        if target != "." and self.get_piece_colour(piece) == self.get_piece_colour(target): # can't capture your own piece
            return False
        
        if piece.lower() == "p":
            return self.is_valid_pawn_move(piece, start, end)
        
        if piece.lower() == "n":
            return self.is_valid_knight_move(piece, start, end)
        
        if piece.lower() == "b":
            return self.is_valid_bishop_move(piece, start, end)
        
        return False
    
    def is_valid_pawn_move(self, piece, start, end):
        sr, sc = start
        er, ec = end

        direction = -1 if piece.isupper() else 1 # white moves up, black moves down

        start_row_white = 6
        start_row_black = 1

        target = self.board[er][ec]

        # --------------------------
        # 1. Forward move (one step)
        # --------------------------

        if ec == sc and er == sr + direction:
            if target == ".":
                return True
            

        # --------------------------
        # 2. Forward move (2 steps)
        # --------------------------

        if ec == sc and er == sr + 2 * direction:
            if piece.isupper() and sr == start_row_white:
                if self.board[sr + direction][sc] == "." and target == ".":
                    return True

            if piece.islower() and sr == start_row_black:
                if self.board[sr + direction][sc] == "." and target == ".":
                    return True
                
        # -----------------------
        # 3. Diagonal capture
        # -----------------------
        if abs(ec - sc) == 1 and er == sr + direction:
            if target != "." and self.get_piece_colour(target) != self.get_piece_colour(piece):
                return True

        return False
    

    def is_valid_knight_move(self, piece, start, end):
        sr, sc = start
        er, ec = end

        dr = abs(er - sr)
        dc = abs(ec - sc)

        return (dr, dc) in [(2, 1), (1, 2)]
    
    def is_valid_bishop_move(self, piece, start, end):
        sr, sc = start
        er, ec = end

        dr = er - sr
        dc = ec - sc

        if abs(dr) != abs(dc): # ensuring diagonal movement
            return False
        
        row_step = 1 if dr > 0 else -1 # determine the direction of movement
        col_step = 1 if dc > 0 else -1

        r, c = sr + row_step, sc + col_step # start stepping from the square next to the bishop

        while (r, c) != (er, ec): # walk until we reach the destination (excluding it)
            if self.board[r][c] != ".":
                return False  # something is blocking the path
            r += row_step
            c += col_step

        return True
    
    def is_valid_rook_move(self, piece, start, end):
        sr, sc = start
        er, ec = end

        if sr != er and sc != ec: # ensure straight line movement
            return False

        
        if sr == er: # determine direction
            row_step = 0 # hor
            col_step = 1 if ec > sc else -1
        else:
            col_step = 0 # vert
            row_step = 1 if er > sr else -1

        r = sr + row_step # start one square away from the rook
        c = sc + col_step

        while (r, c) != (er, ec): # walk to destination
            if self.board[r][c] != ".":
                return False
            r += row_step
            c += col_step

        return True









