"""
Chess GUI Module

This module provides a graphical user interface for the chess game using pygame.

It is responsible for:
- Initialising the pygame window and display
- Rendering the chessboard and pieces
- Handling user input (mouse clicks and window events)
- Translating user interactions into game actions on the Board object

Key Components:
- draw_board(): Renders the 8x8 chessboard with alternating square colours
- draw_pieces(): Draws chess pieces based on the current board state
- images dictionary: Stores and manages loaded piece images
- Event loop: Handles user input such as quitting the game and (future) piece movement

Architecture Note:
This module is strictly the presentation layer. It does not implement chess rules or game logic.
All game state and move handling is delegated to the Board class in board.py.

The separation of GUI and game logic allows the chess engine to be extended independently
(e.g., adding AI, move validation, or different interfaces) without modifying the rendering code.
"""


import pygame
from board import Board

WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8

WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

images = {
    "P": pygame.transform.scale(pygame.image.load("chess/assets/white-pawn.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "p": pygame.transform.scale(pygame.image.load("chess/assets/black-pawn.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "R": pygame.transform.scale(pygame.image.load("chess/assets/white-rook.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "r": pygame.transform.scale(pygame.image.load("chess/assets/black-rook.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "N": pygame.transform.scale(pygame.image.load("chess/assets/white-knight.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "n": pygame.transform.scale(pygame.image.load("chess/assets/black-knight.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "B": pygame.transform.scale(pygame.image.load("chess/assets/white-bishop.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "b": pygame.transform.scale(pygame.image.load("chess/assets/black-bishop.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "Q": pygame.transform.scale(pygame.image.load("chess/assets/white-queen.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "q": pygame.transform.scale(pygame.image.load("chess/assets/black-queen.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "K": pygame.transform.scale(pygame.image.load("chess/assets/white-king.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE)),
    "k": pygame.transform.scale(pygame.image.load("chess/assets/black-king.png").convert_alpha(), (SQUARE_SIZE, SQUARE_SIZE))
}

board = Board()

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 ==0 else BROWN
            pygame.draw.rect(
                screen,
                color,
                (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

def draw_pieces():
    for row in range(8):
        for col in range(8):
            piece = board.get_piece(row, col)
            if piece != ".":
                screen.blit(images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()