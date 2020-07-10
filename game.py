import pygame
from board import Board

BLACK = (0, 0, 0)
WIDTH = HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
clock.tick(5)
pygame.display.set_caption("Tic-Tac-Toe")

def main_menu() -> None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_1:
                    # TODO Make single player vs Bot
                if event.key == pygame.K_2:
                    game_loop()
        screen.fill((215, 215, 215))
        font = pygame.font.Font(pygame.font.get_default_font(), 24)
        # text1 = font.render("Press 1 for Single Player Mode", 1, BLACK)/
        text2 = font.render("Press 2 for 2-Player Mode", 1, BLACK)
        instr = font.render("Press 'R' to restart at any point", 1, BLACK)

        # screen.blit(text1, (int(WIDTH / 2 - text1.get_width() / 2), HEIGHT / 2 - 40))
        # screen.blit(text2, (int(WIDTH / 2 - text2.get_width() / 2), HEIGHT / 2 + 40))
        screen.blit(text2, (int(WIDTH / 2 - text2.get_width() / 2), HEIGHT / 2))
        screen.blit(instr, (int(WIDTH / 2 - instr.get_width() / 2), HEIGHT - 35))
        pygame.display.update()


def game_loop() -> None:
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

        board.check_if_over()


if __name__ == "__main__":
    pygame.init()
    main_menu()
