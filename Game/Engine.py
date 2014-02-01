import pygame
from Game.Shared.GameConstants import *
from Molarr import Molarr
import sys
import warnings


class Engine(object):

    def __init__(self):

        self.player = None
        self.playerGroup = pygame.sprite.GroupSingle()
        self.candies = pygame.sprite.Group()
        self.score = 0

        self.screen = None
        self.clock = None

        self.eventHandlers = [self.handleEvents]

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    def startGame(self):

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.player = Molarr(self)

        while True:
            self.clock.tick(MAX_FPS)

            #print len(self.eventHandlers)
            handlers_to_remove = []
            events = pygame.event.get()

            for handler in self.eventHandlers:
                try:
                    handler(events)
                except Exception as e:
                    warnings.warn("WARNING: Found zombie event handler. Removing...")
                    handlers_to_remove.append(handler)

            for handler in handlers_to_remove:
                self.eventHandlers.remove(handler)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            self.screen.fill(BLACK)

            self.player.move()

            self.player.hammer.update()

            self.player.render()

            pygame.display.update()






