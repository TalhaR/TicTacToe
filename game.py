import pygame


SIZE = (500, 500)

pygame.init()
screen = pygame.display.set_mode(SIZE)

while(True):
    pygame.time.delay(100)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.exit()

    cRec = pygame.draw.circle(screen, (0, 0, 255), (100, 100), 100, 10)
    pygame.draw.circle(screen, (0, 0, 255), cRec)

    pygame.display.update()
