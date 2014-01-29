from Game.Shared.GameConstants import *
import numpy as np
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, engine, image, velocity, maxSpeed,
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
        self.maxSpeed = maxSpeed

        self.image = image
        self.destination = None

        if destination is not None:
            self.destination = np.array(destination, np.int32)

        self.size = self.image.get_size()

    def getPosition(self):
        return np.array([self.rect.x, self.rect.y], np.int32)

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def outOfBoundsLeft(self):
        return self.rect.x < 0

    def outOfBoundsTop(self):
        return self.rect.y < 0

    def outOfBoundsRight(self):
        return self.rect.x - self.size[0] > SCREEN_SIZE[0]

    def outOfBoundsBottom(self):
        return self.rect.y - self.size[1] > SCREEN_SIZE[1]

    def keepInWindow(self):
        if self.outOfBoundsLeft():
            self.velocity[0] *= -1
            self.rect.x = 0

        if self.outOfBoundsTop():
            self.velocity[1] *= -1
            self.rect.y = 0

        if self.outOfBoundsRight():
            self.rect.x = SCREEN_SIZE[0] - self.size[0]
            self.velocity[0] *= -1

        if self.outOfBoundsBottom():
            self.rect.y = SCREEN_SIZE[1] - self.size[1]
            self.velocity[1] *= -1

    def move(self):
        if self.destination is not None:
            v = self.destination.astype(np.float64) - self.getPosition().astype(np.float64)
            #print "v: " + str(v.tolist())
            length = np.linalg.norm(v)

            if length > 0:
                v /= np.linalg.norm(v)
                v *= self.maxSpeed

                self.velocity = np.round(v).astype(np.int32)

        self.setPosition(self.getPosition() + self.velocity)
        self.keepInWindow()

    def render(self):

        self.engine.screen.blit(self.image, self.getPosition())







