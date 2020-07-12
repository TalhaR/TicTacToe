import pygame
from board import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

def main_menu() -> None:
    font = pygame.font.Font(pygame.font.get_default_font(), 48)
    text1 = font.render("1: Local 2-Player Mode", 1, BLACK)
    text2 = font.render("2: LAN 2-Player Mode", 1, BLACK)
    instr = font.render("Press 'R' to restart", 1, BLACK)

    x_pos = lambda obj: WIDTH // 2 - obj.get_width() // 2
    dimensions = lambda obj: (obj.get_width(), obj.get_height())
    button1 = pygame.Rect((x_pos(text1), HEIGHT // 2 - 75), dimensions(text1))
    button2 = pygame.Rect((x_pos(text2), HEIGHT // 2 + 50), dimensions(text2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop()
                # if event.key == pygame.K_2:
                    # TODO Make LAN Functionality
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint((event.pos)):
                    game_loop()
                # if button2.collidepoint((event.pos)):
                    # TODO Make LAN Functionality
        screen.fill((220, 220, 220))
        pygame.draw.rect(screen, WHITE, button1)
        pygame.draw.rect(screen, WHITE, button2)
        screen.blit(text1, (x_pos(text1), HEIGHT // 2 - 75))
        screen.blit(text2, (x_pos(text2), HEIGHT // 2 + 50))
        screen.blit(instr, (x_pos(instr), HEIGHT - 50))
        pygame.display.update()

def game_loop() -> None:
    # back-end matrix for determining game logic
    board = Board()

    while True:
        pygame.time.delay(100)
        screen.fill(BLACK)
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
