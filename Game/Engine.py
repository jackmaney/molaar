import pygame
from Game.Shared.GameConstants import *
from Molarr import Molarr
from Candy import Candy
import sys
import warnings
import os


class Engine(object):

    def __init__(self):

        self.player = None
        self.playerGroup = None
        self.candies = pygame.sprite.Group()

        self.allCandies = [pygame.image.load(img) for img in CANDY_FILES]

        self.score = 0

        self.screen = None
        self.clock = None

        self.eventHandlers = [self.handleEvents]

        self.player = Molarr(self)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    def startGame(self):

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        candy = Candy(self)

        while True:
            self.clock.tick(MAX_FPS)

            # print len(self.eventHandlers)
            handlers_to_remove = []
            events = pygame.event.get()

            for handler in self.eventHandlers:
                try:
                    handler(events)
                except Exception as e:
                    warnings.warn(
                        "WARNING: Found zombie event handler. Removing...")
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

            if pygame.sprite.collide_rect(self.player, candy):
                if self.player.bodyRect().colliderect(candy.rect):
                    print "Body Blow!"
                elif self.player.hammer.isSwinging and self.player.hammer.headRect().colliderect(candy.rect):
                    print "Hammer hit!"
                else:
                    print "General collision"

            self.player.render()

            candy.render()

            pygame.display.update()
