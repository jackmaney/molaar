import pygame
from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
from random import choice


class Candy(Entity):

    def __init__(self, engine, image=None, velocity=(0, 0), maxSpeed=20,
                 initialPosition=(500, 500), destination=None, health=1):

        self.engine = engine

        if image is None:
            self.image = choice(self.engine.allCandies)
        else:
            self.image = image

        Entity.__init__(self, engine, self.image,
                        velocity, maxSpeed, initialPosition, destination, health)
