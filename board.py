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
        sr, sc = start             # define the starting and ending sqaures using the row and column
        er, ec = end

        piece = self.board[sr][sc] # access the piece in the selected square
        self.board[sr][sc] = "."   # replace the starting square with an empty square
        self.board[er][ec] = piece # place the selected piece in the chosen square