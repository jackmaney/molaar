import Game.Shared.Entity as Entity
import pygame
import numpy as np


class Molaar(Entity):
    def __init__(self, game, position, sprite=None, velocity=(0, 0),
                 maxSpeed=20, destination=None, health=100):

        self.sprite = None

        if sprite is None:
            self.sprite = pygame.image.load(game.images["Mo'Larr"]["hammers_up"])
        else:
            self.sprite = sprite

        super(Molaar, self).__init__(game, position, self.sprite, velocity, maxSpeed, destination, health)

    def move(self):
        mousePosition = np.array(pygame.mouse.get_pos(), np.int32)
        print "position: " + str(self.position)
        print "mousePosition: " + str(mousePosition)
        if any(self.position != mousePosition):
            self.destination = mousePosition
            #print "Destination: " + str(self.destination.tolist())
            super(Molaar, self).move()