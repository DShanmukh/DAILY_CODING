import pygame

# Initialize pygame
pygame.init()

# Set width, height, and other screen properties
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Chess Game')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# Game variables
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn'] * 2
white_locations = [(x, 0) for x in range(8)] + [(x, 1) for x in range(8)]
black_pieces = white_pieces[:]
black_locations = [(x, 7) for x in range(8)] + [(x, 6) for x in range(8)]
captured_pieces_white, captured_pieces_black = [], []

turn_step = 0  # Track game phase (0: white selects, 1: white moves, 2: black selects, 3: black moves)
selection = 100
valid_moves = []
counter, winner = 0, ''
game_over = False

# Load images
def load_image(path, size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

def load_all_images():
    img_paths = {
        'black': ['black king', 'black queen', 'black rook', 'black bishop', 'black knight', 'black pawn'],
        'white': ['white king', 'white queen', 'white rook', 'white bishop', 'white knight', 'white pawn']
    }
    images = {}
    for color in img_paths:
        for img_name in img_paths[color]:
            large = load_image(f'./images/{img_name}.png', (80, 80))
            small = pygame.transform.scale(large, (45, 45))
            images[f'{color}_{img_name}'] = (large, small)
    return images

images = load_all_images()
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# Drawing functions
def draw_board():
    for i in range(32):
        column, row = i % 4, i // 4
        color = 'light gray'
        pygame.draw.rect(screen, color, [(600 if row % 2 == 0 else 700) - (column * 200), row * 100, 100, 100])
    pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
    pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
        pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
    screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))

def draw_pieces():
    for i, piece in enumerate(white_pieces):
        pos, img_type = white_locations[i], piece_list.index(piece)
        img = images[f'white_{piece_list[img_type]}'][0] if piece != 'pawn' else images['white_pawn'][0]
        screen.blit(img, (pos[0] * 100 + 10, pos[1] * 100 + 10))
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, 'red', [pos[0] * 100 + 1, pos[1] * 100 + 1, 100, 100], 2)
    for i, piece in enumerate(black_pieces):
        pos, img_type = black_locations[i], piece_list.index(piece)
        img = images[f'black_{piece_list[img_type]}'][0] if piece != 'pawn' else images['black_pawn'][0]
        screen.blit(img, (pos[0] * 100 + 10, pos[1] * 100 + 10))
        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, 'blue', [pos[0] * 100 + 1, pos[1] * 100 + 1, 100, 100], 2)

def draw_valid(moves):
    color = 'red' if turn_step < 2 else 'blue'
    for move in moves:
        pygame.draw.circle(screen, color, (move[0] * 100 + 50, move[1] * 100 + 50), 5)

def draw_captured():
    for i, piece in enumerate(captured_pieces_white):
        img = images[f'black_{piece_list.index(piece)}'][1]
        screen.blit(img, (825, 5 + 50 * i))
    for i, piece in enumerate(captured_pieces_black):
        img = images[f'white_{piece_list.index(piece)}'][1]
        screen.blit(img, (925, 5 + 50 * i))

def draw_check():
    if turn_step < 2 and 'king' in white_pieces:
        king_location = white_locations[white_pieces.index('king')]
        if king_location in sum(black_options, []):
            pygame.draw.rect(screen, 'dark red', [king_location[0] * 100 + 1, king_location[1] * 100 + 1, 100, 100], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (210, 240))

# Check functions
def check_options(pieces, locations, turn):
    all_moves_list = []
    for i, piece in enumerate(pieces):
        if piece == 'pawn':
            moves_list = check_pawn(locations[i], turn)
        elif piece == 'rook':
            moves_list = check_rook(locations[i], turn)
        elif piece == 'knight':
            moves_list = check_knight(locations[i], turn)
        elif piece == 'bishop':
            moves_list = check_bishop(locations[i], turn)
        elif piece == 'queen':
            moves_list = check_queen(locations[i], turn)
        elif piece == 'king':
            moves_list = check_king(locations[i], turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# Define check piece move functions for king, queen, bishop, rook, pawn, knight

# Main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True

while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Add event handling code for move selection and execution

pygame.quit()
