import pygame
from Game.Shared.GameConstants import *
import math


class Hammer(object):
    def __init__(self, molarr):

        self.molarr = molarr
        self.image = pygame.transform.rotate(pygame.image.load(HAMMER_IMG), HAMMER_INITIAL_ROTATION_ANGLE)
        self.original = self.image.copy()
        self.rect = self.image.get_rect()
        self.isSwinging = False
        self.swingFrameCounter = 0  # To keep track of which animation frame we're on
        self.isMovingDown = True  # Toggles whether the hammer is going down or going back up

    def update(self):
        if self.isSwinging:

            numFrames = len(self.molarr.frames)

            if self.swingFrameCounter >= numFrames:
                self.isMovingDown = False
                self.swingFrameCounter = numFrames - 1
            elif self.swingFrameCounter < 0:
                self.isMovingDown = True
                self.swingFrameCounter = 0
                self.isSwinging = False


            self.molarr.image = self.molarr.frames[self.swingFrameCounter]

            if self.isMovingDown:
                self.swingFrameCounter += 1
            else:
                self.swingFrameCounter -= 1




