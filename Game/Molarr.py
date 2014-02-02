from Game.Shared.Entity import Entity
from Game.Shared.GameConstants import *
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
            self.image = self.frames[0]
        else:
            self.image = image

        # Keeps track of whether or not Mo'Larr is swinging his hammer
        self.isSwinging = False
        # To keep track of which animation frame we're on
        self.swingFrameCounter = 0
        # Toggles whether the hammer is going down or going back up
        self.isSwingingDown = True

        self.engine.eventHandlers = [self.handleEvents] + \
            self.engine.eventHandlers

        # Are we facing right or left?
        self.facingRight = True
        # Signals to the renderer that the direction has changed
        self.flipImage = False
        # If true, there is no flipping
        self.overrideFlip = False

        Entity.__init__(self, engine, self.image,
                        velocity, maxSpeed, (0, 0), destination, health)

    def handleEvents(self, events):
        pressed = self.engine.pressedKeys

        self.overrideFlip = pressed[pygame.K_LSHIFT]

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.isSwinging = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.overrideFlip:
                    self.flipImage = True

    def update(self):

        self.move()

        if self.isSwinging:
            self.advanceAnimationIndex()

            if self.facingRight:
                self.image = self.frames[self.swingFrameCounter]
            else:
                self.image = pygame.transform.flip(self.frames[self.swingFrameCounter], True, False)

    def move(self):
        mousePosition = np.array(pygame.mouse.get_pos(), np.int32)

        displacement = mousePosition - self.centerOfBody()

        dist = np.linalg.norm(displacement)

        if dist > TURN_THRESHOLD:
            if (displacement[0] < 0 and self.facingRight) or \
                    (displacement[0] > 0 and not self.facingRight):
                self.flipImage = True

        self.setPosition(self.getPosition() + displacement)
        self.keepInWindow()

    def hammerHeadRect(self):
        pos = self.getPosition()
        index = self.swingFrameCounter

        hammerHeadRectPos = HAMMER_COLLISION_RECTS[index]["position"]
        size = HAMMER_COLLISION_RECTS[index]["size"]

        y = pos[1] + hammerHeadRectPos[1]

        if self.facingRight:
            x = pos[0] + hammerHeadRectPos[0]
        else:
            x = pos[0] + self.rect.width - hammerHeadRectPos[0] - size[0]

        return pygame.Rect((x, y), size)

    def bodyRect(self):
        if self.facingRight:
            return pygame.Rect((self.rect.left, self.rect.bottom - MOLARR_SIZE[1]), MOLARR_SIZE)
        else:
            return pygame.Rect((self.rect.left + self.rect.width - MOLARR_SIZE[0], self.rect.bottom - MOLARR_SIZE[1]), MOLARR_SIZE)

    def centerOfBody(self):
        return self.bodyRect().center

    def outOfBoundsLeft(self):
        if self.facingRight:
            return self.rect.x < 0
        else:
            return self.bodyRect().x < 0

    def outOfBoundsRight(self):
        if self.facingRight:
            return self.bodyRect().x + MOLARR_SIZE[0] > SCREEN_SIZE[0]
        else:
            return self.rect.x + self.rect.width > SCREEN_SIZE[0]

    def outOfBoundsTop(self):
        return self.bodyRect().y < 0

    def outOfBoundsBottom(self):
        bodyRect = self.bodyRect()
        return bodyRect.y + bodyRect.height > SCREEN_SIZE[1]

    def keepInWindow(self):
        bodyRect = self.bodyRect()

        if self.outOfBoundsLeft():
            if self.facingRight:
                self.rect.x = 0
            else:
                self.rect.x = -1 * (self.rect.width - bodyRect.width)

        if self.outOfBoundsTop():
            self.rect.y = -1 * (self.rect.height - bodyRect.height)

        if self.outOfBoundsRight():
            if self.facingRight:
                self.rect.x = SCREEN_SIZE[0] - bodyRect.width
            else:
                self.rect.x = SCREEN_SIZE[0] - self.rect.width

        if self.outOfBoundsBottom():
            self.rect.y = SCREEN_SIZE[1] - self.rect.height

    def render(self):
        if self.flipImage and not self.overrideFlip:
            self.facingRight = not self.facingRight

            if self.facingRight:
                self.rect.x += self.rect.width - MOLARR_SIZE[0]
            else:
                self.rect.x -= self.rect.width - MOLARR_SIZE[0]
            self.image = pygame.transform.flip(self.image, True, False)

            self.flipImage = False

        self.engine.screen.blit(self.image, self.rect.topleft)

    def advanceAnimationIndex(self):
        numFrames = len(self.frames)

        if self.isSwinging:

            if self.isSwingingDown:
                self.swingFrameCounter += 1

                if self.swingFrameCounter >= numFrames:
                    self.isSwingingDown = False
                    self.swingFrameCounter = numFrames - 1

            else:
                self.swingFrameCounter -= 1

                if self.swingFrameCounter < 0:
                    self.isSwingingDown = True
                    self.isSwinging = False
                    self.swingFrameCounter = 0




