import pygame
from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
from random import choice, randint
import numpy as np


class Candy(Entity):
    def __init__(self, engine, image=None, maxSpeed=None, health=1, isSeeker=None):

        self.engine = engine

        self.damage = self.engine.timeKeeper.candyDamage()

        if maxSpeed is None:
            self.maxSpeed = self.engine.timeKeeper.candySpeed()
        else:
            self.maxSpeed = maxSpeed

        self.destination = None

        if isSeeker is None:
            self.isSeeker = self.engine.timeKeeper.isCandyASeeker()
        else:
            self.isSeeker = isSeeker

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
        velocity *= self.maxSpeed

        self.velocity = np.round(velocity).astype(np.int32)

        self.initialPosition = (x, y)

        Entity.__init__(self, engine, self.image,
                        self.velocity, self.maxSpeed, self.initialPosition,
                        destination=self.destination, health=health)

    def update(self):
        if self.isSeeker:
            velocity = np.array(self.engine.player.centerOfBody(), np.float64) - \
                np.array(self.getCenter(), np.float64)

            velocity /= np.linalg.norm(velocity)
            velocity *= self.maxSpeed

            self.velocity = velocity


        Entity.update(self)
