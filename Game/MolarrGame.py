import pygame
from Game.Shared import GameConstants
from Game.Molarr import Molaar as m


class Game(object):
    def __init__(self):

        self.paused = True

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("The Saga of Mo'Laar the Barbarian, Crusher of Candies")

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        sprite = pygame.image.load(GameConstants.MOLARR_HAMMERS_UP_IMG)

        self.molarr = m(self, [100, 100], sprite=sprite)

    def start(self):

        while True:
            self.clock.tick(60)

            self.screen.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            self.molarr.move()
            self.molarr.render()

            pygame.display.update()