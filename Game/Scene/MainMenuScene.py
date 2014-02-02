from Game.Scene import Scene
from Game.Shared.GameConstants import *
import pygame


class MainMenuScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)

        self.addCenteredText("The Saga of", 20, size=28)
        self.addCenteredText("Mo'Larr The Barbarian", 80, size=60)
        self.addCenteredText("Crusher of Candies!", 150, size=60)
        self.addCenteredText("(Press any key to start)", 300, size=20)

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.stop()
                self.engine.changeScene("playGame")

    def render(self):
        self.engine.screen.fill(BLACK)

        Scene.render(self)



