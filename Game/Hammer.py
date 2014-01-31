import pygame
from Game.Shared.GameConstants import *
import math


class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.rotate(pygame.image.load(HAMMER_IMG), HAMMER_INITIAL_ROTATION_ANGLE)
        self.original = self.image.copy()
        self.rect = self.image.get_rect()
        self.isSwinging = False
        self.angleIncrementCounter = 1  # multiplier for increment swing angle
        self.isMovingDown = True  #Toggles whether the hammer is going down or going back up

    def update(self):
        if self.isSwinging:

            if self.angleIncrementCounter >= HAMMER_NUM_INCREMENTS_IN_SWING:
                self.isMovingDown = False
                self.angleIncrementCounter == HAMMER_NUM_INCREMENTS_IN_SWING
            elif self.angleIncrementCounter <= 0:
                self.isMovingDown = True
                self.angleIncrementCounter = 1
                self.isSwinging = False

            topleft = [self.rect.topleft[0], self.rect.topleft[1]]
            angle = -1 * self.angleIncrementCounter * HAMMER_ANGLE_INCREMENT_AMOUNT


            self.image = pygame.transform.rotate(self.original, angle)
            self.rect = pygame.Rect(topleft, self.image.get_size())


            if self.isMovingDown:
                self.angleIncrementCounter += 1
            else:
                self.angleIncrementCounter -= 1




