import pygame
from Game.Shared.GameConstants import *
from Game.Scene import *
from Molarr import Molarr
from Candy import Candy
import warnings


class Engine(object):

    def __init__(self):

        self.score = 0
        self.gameTimer = 0

        self.player = None
        self.playerGroup = None
        self.candies = pygame.sprite.Group()

        self.allCandies = [pygame.image.load(img) for img in CANDY_FILES]

        self.score = 0

        self.screen = None
        self.clock = None

        self.handlersToRemove = []

        self.player = Molarr(self)

        self.pressedKeys = None

        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        impactSound = pygame.mixer.Sound(SOUND_IMPACT_FILE)

        self.sounds = {
            "impact": impactSound
        }

        self.loadEnemyTimer = 0

        self.scenes = {
            "mainMenu": MainMenuScene,
            "playGame": GameScene,
            "gameOver": GameOverScene
        }

        self.currentScene = MainMenuScene(self)

    def resetGame(self):
        self.score = 0
        self.gameTimer = 0
        self.player.health = 100
        self.changeScene("playGame")


    def changeScene(self, sceneName):
        self.handlersToRemove.append(self.currentScene.handleEvents)

        self.currentScene = self.scenes[sceneName](self)

    def playSound(self, soundName):
        sound = self.sounds[soundName]
        sound.stop()
        sound.play()

    def loadEnemies(self):
        #print self.gameTimer
        futureThresholds = [n for n in MAX_CANDY_THRESHOLDS if n >= self.gameTimer]

        numEnemies = None

        if len(futureThresholds) == 0:
            numEnemies = MAX_CANDY_THRESHOLDS[max(MAX_CANDY_THRESHOLDS.keys())]
        else:
            numEnemies = MAX_CANDY_THRESHOLDS[min(futureThresholds)]

        # print numEnemies

        while len(self.candies) < numEnemies:
            self.candies.add(Candy(self))

    def startGame(self):



        print len(self.candies)

        while True:
            self.clock.tick(MAX_FPS)

            self.gameTimer += self.clock.get_time()

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
