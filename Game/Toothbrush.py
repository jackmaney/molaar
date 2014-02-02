from Game.Shared.GameConstants import *
from Game.Shared.Entity import Entity
from random import randint

class Toothbrush(Entity):
    def __init__(self, engine):
        self.engine = engine
        self.image = pygame.image.load(TOOTHBRUSH_IMG)
        self.rect = self.image.get_rect()

        x = randint(0, SCREEN_SIZE[0] - self.rect.width)
        y = randint(0, SCREEN_SIZE[1] - self.rect.height)

        self.initialPosition = [x, y]

        Entity.__init__(self, engine, self.image, [0, 0], 0, self.initialPosition)
