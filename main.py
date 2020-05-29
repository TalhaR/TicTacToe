import sys
import pygame
from board import Board

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (215, 215, 215)
BLUE = (0, 0, 255)

# contains background tiles
tiles = []
# will hold player moves ie. X or O
player_moves = []
circle, x_mark = None, None

# keeps track of which player's turn it is
x_turn = True

# back-end matrix for determining game logic
board = Board()


def load_assets():
    # creates 9 rectangles to place on screen
    for i in (0, 210, 420):
        for j in (0, 210, 420):
            tiles.append(pygame.Rect(j, i, 200, 200))
    # loads circle and x_mark assets
    global circle, x_mark
    circle = pygame.image.load('assets/circle.png')
    circle = pygame.transform.scale(circle, (195, 195))
    x_mark = pygame.image.load('assets/X.png')
    x_mark = pygame.transform.scale(x_mark, (195, 195))


def main():
    # 5 fps because tic-tac-toe doesn't benefit
    # from a higher framerate
    clock = pygame.time.Clock()
    clock.tick(5)
    pygame.display.set_caption("Tic-Tac-Toe")
    load_assets()

    while True:
        pygame.time.delay(100)
        screen.fill(BLACK)
        update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for index, rect in enumerate(tiles):
                    if rect.collidepoint(x, y):
                        print(index)

                        x2, y2 = rect.topleft
                        if x_turn:
                            draw_obj(x_mark, index, (x2 + 3, y2 + 3))
                        else:
                            draw_obj(circle, index, (x2 + 3, y2 + 3))


def draw_obj(obj, index, center):
    row = index // 3
    col = index % 3

    global x_turn
    # only place "X" or "O" if the
    # original place is empty ("_")
    if board.place(row, col, x_turn):
        player_moves.append((obj, center))
        print(board)
        x_turn = not x_turn


def update():
    # Draws 9 Rectangles onto the screen
    for rect in tiles:
        pygame.draw.rect(screen, COLOR, rect)
    # Draws all player moves made
    for obj in player_moves:
        screen.blit(obj[0], obj[1])

    # pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 200), 15)

    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    # Size of window
    SIZE = (620, 620)
    screen = pygame.display.set_mode(SIZE)

    main()
