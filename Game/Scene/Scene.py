from Game.Shared.GameConstants import *


class Scene(object):
    def __init__(self, engine):
        self.engine = engine
        self.texts = []
        pygame.font.init()

    def addText(self, text, position, color=WHITE, background=None, size=17):
        font = pygame.font.Font(None, size)
        self.texts.append({"text": font.render(text, True, color, background), "position": position})

    def addCenteredText(self, text, y, color=WHITE, background=None, size=17):
        font = pygame.font.Font(pygame.font.match_font("Georgia"), size)
        renderedText = font.render(text, True, color, background)
        width = renderedText.get_rect().width
        position = (int(SCREEN_SIZE[0] / 2.0) - int(width / 2.0), y)
        self.texts.append({"text": renderedText, "position": position})

    def render(self):
        for text in self.texts:
            self.engine.screen.blit(text["text"], text["position"])

    def update(self):
        pass

    def handleEvents(self, events):
        pass