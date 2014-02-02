import pygame
from Game.Shared.GameConstants import *
from Game.Scene import *
from Molarr import Molarr
from Candy import Candy
import warnings


class Engine(object):

    def __init__(self):

        self.player = None
        self.playerGroup = None
        self.candies = pygame.sprite.Group()

        self.allCandies = [pygame.image.load(img) for img in CANDY_FILES]

        self.score = 0

        self.screen = None
        self.clock = None

        self.eventHandlers = [self.handleEvents]
        self.handlersToRemove = []

        self.player = Molarr(self)

        self.pressedKeys = None

        pygame.init()
        pygame.mixer.init()

        impactSound = pygame.mixer.Sound(SOUND_IMPACT_FILE)

        self.sounds = {
            "impact": impactSound
        }

        self.loadEnemyTimer = 0

        self.scenes = {
            "mainMenu": MainMenuScene,
            "playGame": GameScene
        }

        self.currentScene = MainMenuScene(self)

    def changeScene(self, sceneName):
        self.handlersToRemove.append(self.currentScene.handleEvents)

        self.currentScene = self.scenes[sceneName](self)

    def playSound(self, soundName):
        sound = self.sounds[soundName]
        sound.stop()
        sound.play()

    def loadEnemies(self):
        time = pygame.time.get_ticks()
        print time
        futureThresholds = [n for n in MAX_CANDY_THRESHOLDS if n >= time]

        numEnemies = None

        if futureThresholds == []:
            numEnemies = MAX_CANDY_THRESHOLDS[max(MAX_CANDY_THRESHOLDS.keys())]
        else:
            numEnemies = MAX_CANDY_THRESHOLDS[min(futureThresholds)]

        while len(self.candies) < numEnemies:
            self.candies.add(Candy(self))

    def handleEvents(self, events):
        self.eventHandlers = [h for h in self.eventHandlers if h not in self.handlersToRemove]
        self.handlersToRemove = []
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

    def startGame(self):

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        print len(self.candies)

        while True:
            self.clock.tick(MAX_FPS)

            self.pressedKeys = pygame.key.get_pressed()

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            self.currentScene.handleEvents(events)

            self.screen.blit(BACKGROUND, (0, 0))

            self.currentScene.update()

            self.currentScene.render()

            pygame.display.update()
