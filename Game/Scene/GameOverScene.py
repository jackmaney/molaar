from Game.Scene import Scene
from Game.Shared.GameConstants import *
import pygame


class GameOverScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)
        self.addCenteredText("Game Over!", 100, size=72)
        self.addCenteredText("Your score was: " + str(self.engine.score), 250, size=30)

        numSeconds = round(float(self.engine.timeKeeper.timer) / 1000, 1)

        self.addCenteredText("You managed to last: " + str(numSeconds) + " seconds", 320, size=30)
        self.addCenteredText("Press Escape to quit, or any other key to start a new game", 450, size=30)

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
                else:
                    self.engine.resetGame()

    def render(self):
        self.engine.screen.fill(BLACK)

        Scene.render(self)

