from Game.Shared.GameConstants import *
import numpy as np
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, engine, image, velocity, speed,
                 initialPosition, destination=None, health=100, spriteGroup=None):

        if spriteGroup is not None:
            pygame.sprite.Sprite.__init__(self, spriteGroup)
        else:
            pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.setPosition(initialPosition)
        self.velocity = np.array(velocity, np.int32)

        self.engine = engine
        self.health = health
        self.maxSpeed = speed

        self.image = image
        self.destination = None

        if destination is not None:
            self.destination = np.array(destination, np.int32)

        self.size = np.array(self.image.get_size(), np.int32)

    def getPosition(self):
        return np.array(self.rect.topleft, np.int32)

    def getCenter(self):
        return np.ceil(self.getPosition() + self.rect.size / 2.0).astype(np.int32)

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def outOfBoundsLeft(self):
        return self.rect.x < 0

    def outOfBoundsTop(self):
        return self.rect.y < 0

    def outOfBoundsRight(self):
        return self.rect.x + self.rect.size[0] > SCREEN_SIZE[0]

    def outOfBoundsBottom(self):
        return self.rect.y + self.rect.size[1] > SCREEN_SIZE[1]

    def keepInWindow(self):
        if self.outOfBoundsLeft():
            self.velocity[0] *= -1
            self.rect.x = 0

        if self.outOfBoundsTop():
            self.velocity[1] *= -1
            self.rect.y = 0

        if self.outOfBoundsRight():
            self.rect.x = SCREEN_SIZE[0] - self.rect.size[0]
            self.velocity[0] *= -1

        if self.outOfBoundsBottom():
            self.rect.y = SCREEN_SIZE[1] - self.rect.size[1]
            self.velocity[1] *= -1

    def update(self):

        self.setPosition(self.getPosition() + self.velocity)
        self.keepInWindow()

    def render(self):

        self.engine.screen.blit(self.image, self.getPosition())







