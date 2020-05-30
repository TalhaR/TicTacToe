import pygame
from board import Board


def play():
    # 1 fps because tic-tac-toe doesn't benefit from a higher framerate
    clock = pygame.time.Clock()
    clock.tick(1)
    pygame.display.set_caption("Tic-Tac-Toe")
    # back-end matrix for determining game logic
    board = Board()

    while True:
        pygame.time.delay(100)
        screen.fill((0, 0, 0))
        board.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and not board.match_ended:
                board.make_move(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.clear()
                # if event.key == pygame.K_u:
                #     board.undo()

        board.check_if_over()


if __name__ == "__main__":
    pygame.init()
    # Size of window
    SIZE = (620, 620)
    screen = pygame.display.set_mode(SIZE)

    play()
