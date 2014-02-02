from Game.Shared.GameConstants import *
from Game.Scene import *
from Molarr import Molarr
from Candy import Candy
from Toothbrush import Toothbrush
from TimeKeeper import TimeKeeper

class Engine(object):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.score = 0
        self.timeKeeper = TimeKeeper(self)

        self.player = None
        self.playerGroup = None
        self.candies = pygame.sprite.Group()
        self.toothbrushes = pygame.sprite.Group()

        self.score = 0

        self.screen = None
        self.clock = None

        self.handlersToRemove = []

        self.pressedKeys = None
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        self.clock = pygame.time.Clock()

        self.player = Molarr(self)
        self.allCandies = [pygame.image.load(img).convert_alpha() for img in CANDY_FILES]

        impactSound = pygame.mixer.Sound(SOUND_IMPACT_FILE)
        ductTapeSound = pygame.mixer.Sound(SOUND_DUCT_TAPE_FILE)
        toothbrushSound = pygame.mixer.Sound(SOUND_TOOTHBRUSH)

        self.sounds = {
            "impact": impactSound,
            "ductTape": ductTapeSound,
            "toothbrush": toothbrushSound
        }

        self.baseMolarrImage = pygame.image.load(MOLARR_IMG).convert_alpha()
        self.baseHammerImage = pygame.image.load(HAMMER_IMG).convert_alpha()

        self.loadEnemyTimer = 0
        self.loadToothbrushTimer = 0

        self.scenes = {
            "opening": OpeningCutScene,
            "mainMenu": MainMenuScene,
            "playGame": GameScene,
            "gameOver": GameOverScene
        }

        self.currentScene = self.scenes["opening"](self)

    def resetGame(self):
        self.score = 0
        self.timeKeeper.resetTimer()
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

        numCandies = self.timeKeeper.numCandies()

        while len(self.candies) < numCandies:
            self.candies.add(Candy(self))

    def loadToothbrushes(self):

        numBrushes = self.timeKeeper.numToothbrushes()

        while len(self.toothbrushes) < numBrushes:
            self.toothbrushes.add(Toothbrush(self))

    def startGame(self):

        while True:
            self.clock.tick(MAX_FPS)

            self.timeKeeper.timer += self.clock.get_time()

            self.pressedKeys = pygame.key.get_pressed()

            self.screen.blit(BACKGROUND, (0, 0))

            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            self.currentScene.handleEvents(events)

            self.currentScene.update()

            self.currentScene.render()

            pygame.display.update()

    # Blarg...too lazy to create a Util class for just one function...
    def msToHMS(self, n):
        n //= 1000

        if n < 60:
            return str(int(round(n, 0)))
        elif n < 3600:
            numMin = n // 60
            numLeftOverSec = n - 60 * numMin
            secStr = str(numLeftOverSec)
            if numLeftOverSec < 10:
                secStr = "0" + secStr
            return str(numMin) + ":" + secStr
        else:
            # If you can make it through an entire hour, I salute you...
            numHours = n // 3600
            numLeftOverMinutes = n - numHours // 60
            numLeftOverSec = n - 60 * numLeftOverMinutes

            minStr = str(numLeftOverMinutes)
            if numLeftOverMinutes < 10:
                minStr = "0" + minStr

            secStr = str(numLeftOverSec)
            if numLeftOverSec < 10:
                secStr = "0" + secStr

            return str(numHours) + ":" + minStr + ":" + secStr
