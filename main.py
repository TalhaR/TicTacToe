import sys
import pygame
from board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = (215, 215, 215)
BLUE = (0, 0, 255)

SIZE = (620, 620)
clock = pygame.time.Clock()

circle = pygame.image.load('assets/circle.png')
circle = pygame.transform.scale(circle, (195, 195))

rectangles = []
objects = []

board = Board()


for i in (0, 210, 420):
    for j in (0, 210, 420):
        rectangles.append(pygame.Rect(i, j, 200, 200))


def main():
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
                for index, rect in enumerate(rectangles):
                    if rect.collidepoint(x, y):
                        print(index)
                        draw_circle(index, (rect.topleft[0] + 3, rect.topleft[1] + 3))


def draw_circle(index, center):
    objects.append((circle, center))

    row, col = 0, 0
    if index > 2:
        row = 9 % index + 1
        index = int(9 / index)

    board[row][index] = "O"

    print(board)


def update():
    # win.blit(bg, (0, 0))

    # Draws 9 Rectangles on screen
    for rect in rectangles:
        pygame.draw.rect(screen, COLOR, rect)

    for obj in objects:
        screen.blit(obj[0], obj[1])
    # pygame.draw.circle(screen, BLUE, (99, 99), 100, 10)

    # pygame.draw.line(screen, (0, 0, 255), (0, 0), (200, 200), 15)
    # pygame.draw.line(screen, (0, 0, 255), (200, 0), (0, 200), 15)

    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    main()
