import sys
import pygame
from board import Board

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (215, 215, 215)
BLUE = (0, 0, 255)

SIZE = (620, 620)
clock = pygame.time.Clock()

# loads circle and x_mark assets
circle = pygame.image.load('assets/circle.png')
circle = pygame.transform.scale(circle, (195, 195))
x_mark = pygame.image.load('assets/X.png')
x_mark = pygame.transform.scale(x_mark, (195, 195))

# contain background empty tiles
tiles = []
# will hold player moves ie. X or O
player_moves = []

# keeps track of which player's turn it is
x_turn = True

# back-end matrix for determining game logic
board = Board()

# creates 9 rectangles to place on screen
for i in (0, 210, 420):
    for j in (0, 210, 420):
        tiles.append(pygame.Rect(j, i, 200, 200))


def main():
    # 5 fps because tic-tac-toe doesn't benefit
    # from a higher framerate
    clock.tick(5)
    pygame.display.set_caption("Tic-Tac-Toe")

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
                        global x_turn

                        if not x_turn:
                            draw_obj(circle, index, (rect.topleft[0] + 3, rect.topleft[1] + 3))
                        if x_turn:
                            draw_obj(x_mark, index, (rect.topleft[0] + 3, rect.topleft[1] + 3))
                        x_turn = not x_turn


def draw_obj(obj, index, center):
    row, col = 0, 0
    if index > 2:
        row = index // 3
        index = index % 3

    # only place "X" or "O" if the
    # original place is empty ("_")
    if x_turn:
        if board[row][index] == "_":
            board[row][index] = "X"
            print(board)
            player_moves.append((obj, center))
    else:
        if board[row][index] == "_":
            board[row][index] = "O"
            print(board)
            player_moves.append((obj, center))


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
    screen = pygame.display.set_mode(SIZE)

    main()
