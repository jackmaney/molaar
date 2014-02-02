import pygame
from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
from random import choice, randint, random


class Candy(Entity):

    def __init__(self, engine, image=None, velocity=(0, 0), maxSpeed=20,
                 initialPosition=None, destination=None, health=1):

        self.engine = engine

        if image is None:
            self.image = choice(self.engine.allCandies)
        else:
            self.image = image

        self.rect = self.image.get_rect()

        if initialPosition is None:
            # Equal chance of appearing on the top, right, or bottom sides
            rand = random()
            x, y = (0, 0)

            if rand < 0.33:
                x = randint(0, SCREEN_SIZE[0] - self.rect.width)
            elif rand < 0.66:
                x = SCREEN_SIZE[0] - self.rect.width
                y = randint(0, SCREEN_SIZE[1] - self.rect.height)
            else:
                y = SCREEN_SIZE[1] - self.rect.height
                x = randint(0, SCREEN_SIZE[1] - self.rect.width)

            self.initialPosition = (x, y)
        else:
            self.initialPosition = initialPosition

        Entity.__init__(self, engine, self.image,
                        velocity, maxSpeed, self.initialPosition, destination, health)
