import pygame

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

board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]

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
            piece = board[row][col]
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


