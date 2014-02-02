import pygame
from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
from random import choice, randint
import numpy as np


class Candy(Entity):
    def __init__(self, engine, image=None, maxSpeed=20, health=1, damage=None):

        self.engine = engine

        if damage is None:
            self.damage = randint(1,5)
        else:
            self.damage = damage

        if image is None:
            self.image = choice(self.engine.allCandies)
        else:
            self.image = image

        self.rect = self.image.get_rect()

        # Equal chance of appearing on the top, right, or bottom sides
        rand = randint(1, 3)
        x, y = (0, 0)

        velX = choice(list(range(-10, 0)) + list(range(1, 10)))
        velY = choice(list(range(-10, 0)) + list(range(1, 10)))

        velocity = np.array([velX, velY], np.float64)
        if rand == 1:
            x = randint(0, SCREEN_SIZE[0] - self.rect.width)
            velocity[1] = abs(velocity[1])
        elif rand == 2:
            x = SCREEN_SIZE[0] - self.rect.width
            y = randint(0, SCREEN_SIZE[1] - self.rect.height)
            velocity[0] = abs(velocity[0])
        else:
            y = SCREEN_SIZE[1] - self.rect.height
            x = randint(0, SCREEN_SIZE[1] - self.rect.width)
            velocity[1] = abs(velocity[1])

        velocity /= np.linalg.norm(velocity)
        velocity *= randint(1, maxSpeed)

        self.velocity = np.round(velocity).astype(np.int32)

        self.initialPosition = (x, y)

        Entity.__init__(self, engine, self.image,
                        self.velocity, maxSpeed, self.initialPosition, destination=None, health=health)
