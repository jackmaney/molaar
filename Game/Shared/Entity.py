from Game.Shared import GameConstants
import numpy as np


class Entity(object):
    def __init__(self, game, position, sprite, velocity, maxSpeed, destination=None, health=100):

        self.game = game
        self.position = np.array(position, np.int32)
        self.health = health
        self.maxSpeed = maxSpeed
        self.velocity = np.array(velocity, np.int32)
        self.sprite = sprite
        self.destination = None

        if destination is not None:
            self.destination = np.array(destination, np.int32)

        self.size = self.sprite.get_size()

    def outOfBoundsLeft(self):
        return self.position[0] < 0

    def outOfBoundsTop(self):
        return self.position[1] < 0

    def outOfBoundsRight(self):
        return self.position[0] - self.size[0] > GameConstants.SCREEN_SIZE[0]

    def outOfBoundsBottom(self):
        return self.position[1] - self.size[1] > GameConstants.SCREEN_SIZE[1]

    def keepInWindow(self):
        if self.outOfBoundsLeft():
            self.velocity[0] *= -1
            self.position[0] = 0

        if self.outOfBoundsTop():
            self.velocity[1] *= -1
            self.position[1] = 0

        if self.outOfBoundsRight():
            self.position[0] = GameConstants.SCREEN_SIZE[0] - self.size[0]
            self.velocity[0] *= -1

        if self.outOfBoundsBottom():
            self.position[1] = GameConstants.SCREEN_SIZE[1] - self.size[1]
            self.velocity[1] *= -1

    def move(self):
        if self.destination is not None:
            v = self.destination.astype(float) - self.position.astype(float)
            #print "v: " + str(v.tolist())
            length = np.linalg.norm(v)

            if length > 0:

                v /= np.linalg.norm(v)
                v *= self.maxSpeed

                self.velocity = np.round(v).astype(np.int32)

        self.position += self.velocity
        self.keepInWindow()

    def render(self):

        self.game.screen.blit(self.sprite, self.position)







