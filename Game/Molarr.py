from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
from Game.Hammer import Hammer
import pygame
import numpy as np


class Molarr(Entity):

    def __init__(self, engine, image=None, velocity=(0, 0),
                 maxSpeed=40, destination=None, health=100):

        self.velocity = velocity
        self.sprite = None
        self.engine = engine

        self.frames = [pygame.image.load(img) for img in MOLARR_SWINGING_IMGS]
        if image is None:
            self.image = pygame.image.load(MOLARR_SWINGING_IMGS[0])
        else:
            self.image = image

        self.hammer = Hammer(self)

        self.engine.eventHandlers = [self.handleEvents] + \
            self.engine.eventHandlers

        Entity.__init__(self, engine, self.image,
                        velocity, maxSpeed, (0, 0), destination, health)

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.hammer.isSwinging = True

    def move(self):
        mousePosition = np.array(pygame.mouse.get_pos(), np.int32)

        displacement = mousePosition - self.getPosition()

        if np.linalg.norm(displacement) > MOUSE_MOVEMENT_THRESHOLD:
            v = displacement.astype(float) / np.linalg.norm(displacement)
            v *= self.maxSpeed
            self.velocity = np.round(v).astype(np.int32)

            self.setPosition(self.getPosition() + self.velocity)

    def update(self):
        self.hammer.update()

    def bodyRect(self):

        return pygame.Rect((self.rect.left, self.rect.bottom - MOLARR_SIZE[1]), MOLARR_SIZE)
