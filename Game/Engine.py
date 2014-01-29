import pygame
from Game.Shared.GameConstants import *
from Molarr import Molarr
import sys


class Engine(object):

    def __init__(self):

        self.player = None
        self.playerGroup = pygame.sprite.GroupSingle()
        self.candies = pygame.sprite.Group()
        self.score = 0

        self.screen = None
        self.clock = None

    def startGame(self):

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.player = Molarr(self)

        while True:
            self.clock.tick(MAX_FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.screen.fill(BLACK)

            self.player.move()

            self.player.render()

            pygame.display.update()






