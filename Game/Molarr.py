from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
import pygame
import numpy as np


class Molarr(Entity):
    def __init__(self, engine, image=None, velocity=(0, 0),
                 maxSpeed=40, destination=None, health=100):

        self.velocity = velocity
        self.sprite = None

        if image is None:
            self.image = pygame.image.load(MOLARR_IMG)
        else:
            self.image = image

        Entity.__init__(self, engine, self.image,
                        velocity, maxSpeed, (0, 0), destination, health)

    def move(self):
        mousePosition = np.array(pygame.mouse.get_pos(), np.int32)

        displacement = mousePosition - self.getPosition()

        if np.linalg.norm(displacement) > MOUSE_MOVEMENT_THRESHOLD:
            v = displacement.astype(float) / np.linalg.norm(displacement)
            v *= self.maxSpeed
            self.velocity = np.round(v).astype(np.int32)

            self.setPosition(self.getPosition() + self.velocity)