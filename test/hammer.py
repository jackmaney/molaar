import pygame
from Game.Shared.GameConstants import *
from Game.Hammer import Hammer


def main():

    pygame.init()

    windowSize = (1024, 768)

    screen = pygame.display.set_mode(windowSize)

    clock = pygame.time.Clock()

    hammer = Hammer()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                hammer.isSwinging = True

        screen.fill(BLACK)

        hammer.update()

        screen.blit(hammer.image, [200, 200])

        #print clock.get_fps()

        pygame.display.update()

if __name__ == '__main__':
    main()
