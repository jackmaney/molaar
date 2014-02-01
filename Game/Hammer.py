import pygame
from Game.Shared.GameConstants import *
import math


class Hammer(object):

    def __init__(self, molarr):

        self.molarr = molarr
        self.image = pygame.transform.rotate(
            pygame.image.load(HAMMER_IMG), HAMMER_INITIAL_ROTATION_ANGLE)
        self.original = self.image.copy()
        self.rect = self.image.get_rect()
        self.isSwinging = False
        # To keep track of which animation frame we're on
        self.swingFrameCounter = 0
        # Toggles whether the hammer is going down or going back up
        self.isMovingDown = True

    def headRect(self):
        self.keepIndexInCheck()

        pos = self.molarr.getPosition()

        x = pos[0] + \
            HAMMER_COLLISION_RECTS[self.swingFrameCounter]["position"][0]
        y = pos[1] + \
            HAMMER_COLLISION_RECTS[self.swingFrameCounter]["position"][1]

        size = HAMMER_COLLISION_RECTS[self.swingFrameCounter]["size"]

        return pygame.Rect((x, y), size)

    def update(self):
        if self.isSwinging:

            self.keepIndexInCheck()

            self.molarr.image = self.molarr.frames[self.swingFrameCounter]

            if self.isMovingDown:
                self.swingFrameCounter += 1
            else:
                self.swingFrameCounter -= 1

    def keepIndexInCheck(self):
        numFrames = len(self.molarr.frames)

        if self.swingFrameCounter >= numFrames:
            self.isMovingDown = False
            self.swingFrameCounter = numFrames - 1
        elif self.swingFrameCounter < 0:
            self.isMovingDown = True
            self.swingFrameCounter = 0
            self.isSwinging = False
