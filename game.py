import sys
import pygame
from board import Board

# back-end matrix for determining game logic
board = Board()


def main():
    # 5 fps because tic-tac-toe doesn't benefit
    # from a higher framerate
    clock = pygame.time.Clock()
    clock.tick(1)
    pygame.display.set_caption("Tic-Tac-Toe")

    while True:
        pygame.time.delay(100)
        screen.fill((0, 0, 0))
        board.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not board.match_ended:
                board.make_move(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.create_empty_board()
                    board.player_moves.clear()
                    board.match_ended = False

        if not board.match_ended and board.check_for_winner():
            board.match_ended = True


def winning_animation():
    pass


if __name__ == "__main__":
    pygame.init()
    # Size of window
    SIZE = (620, 620)
    screen = pygame.display.set_mode(SIZE)

    main()
