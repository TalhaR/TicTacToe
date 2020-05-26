import sys
import pygame
# from board import Board

SIZE = (600, 600)
clock = pygame.time.Clock()

bg = pygame.image.load('assets/board.png')
bg = pygame.transform.scale(bg, SIZE)


def main():
    clock.tick(24)

    pygame.display.set_caption("Tic-Tac-Toe")

    color = 215, 215, 215

    while (True):
        pygame.time.delay(100)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()

        win.fill(color)
        update()


def update():
    win.blit(bg, (0, 0))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode(SIZE)

    main()
