import pygame
from Game.Scene import Scene
from Game.Shared.GameConstants import *


class OpeningCutScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)

        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load(OPENING_MUSIC_FILE)
        pygame.mixer.music.play()

        # Number of ms to show text before fading out
        self.timeBeforeBlackOut = 3000
        # Number of ms between screens
        self.timeBetweenScreens = 500

        # Timers
        self.preBlackOutTimer = 0
        self.blackOutTimer = 0

        #Kind of an ugly hack, but I don't have time to refactor all of this properly.
        self.screens = [
            self.screen1,
            self.screen2,
            self.screen3,
            self.screen4,
            self.screen5,
            self.screen6,
            self.screen7,
            self.screen8,
            self.screen9
        ]

        self.images = []
        self.currentScreenIndex = 0

        self.screens[self.currentScreenIndex]()

        self.playingDuctTapeSound = False

    def resetScreen(self):
        self.texts = []
        self.images = []

        if self.playingDuctTapeSound:
            self.engine.sounds["ductTape"].stop()

        self.preBlackOutTimer = 0
        self.blackOutTimer = 0

    def screen1(self):
        self.timeBeforeBlackOut = 5000
        self.addText("Extracted from his home, uprooted from his family", (100, 100), size=30)
        self.addText("a molar wandered amongst a land of sugary sweets.", (100, 160), size=30)
        self.addText("Feeling overwhelmed, he called out to the Goddess Andante.", (100, 220), size=30)


    def screen2(self):
        self.timeBeforeBlackOut = 3000
        self.useMolarr()
        self.addText("\"Andante, She of the Long Tooth,", (675, 400), size=25)
        self.addText("please hear me! I am uprooted and lost!\"", (675, 440), size=25)

    def screen3(self):
        self.useMolarr()
        self.useAndante()

        self.addText("\"I hear your call. This land is overrun with sugar and filth.", (300, 100), size=30)
        self.addText("Become my enameled champion,", (300, 150), size=30)
        self.addText(" and crush all of the candies before you.\"", (300, 200), size=30)

    def screen4(self):
        self.useMolarr()
        self.useAndante()
        self.useHammer()

        self.addText("\"BEHOLD! THE HAMMER OF KREBS!\"", (300, 100), size=30)

    def screen5(self):
        self.useMolarr()
        self.useAndante()
        self.useHammer()

        self.addText("\"Ummm...I...I don't have any arms...\"", (675, 400), size=25)


    def screen6(self):
        self.useMolarr()
        self.useAndante()
        self.useHammer()

        self.addText("\"Oh...right...hold on...\"", (300, 100), size=30)

    def screen7(self):
        self.timeBeforeBlackOut = 10000
        self.engine.playSound("ductTape")
        self.playingDuctTapeSound = True

    def screen8(self):
        self.timeBeforeBlackOut = 3000

        img = self.engine.player.image
        self.images.append({"image": self.engine.player.image,
                            "position": (675, 575 + MOLARR_SIZE[1] - img.get_rect().height)})

        self.useAndante()

        self.addText("\"Perfect! Now, go.\"", (300, 100), size=30)

    def screen9(self):
        self.addCenteredText("And thus began...", 300, size=30)

    def useMolarr(self, position=(600, 500)):
        img = pygame.transform.flip(self.engine.baseMolarrImage, True, False).convert_alpha()
        self.images.append({"image": img, "position": position})

    def useAndante(self):
        img = pygame.image.load(ANDANTE_IMG).convert_alpha()
        self.images.append({"image": img, "position": (0, 0)})

    def useHammer(self):
        img = pygame.transform.flip(pygame.image.load(HAMMER_IMG).convert_alpha(), False, True)
        self.images.append({"image": img, "position": (675, 575)})

    def handleEvents(self, events):

        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                self.resetScreen()

                if self.currentScreenIndex < len(self.screens) - 1:
                    self.currentScreenIndex += 1
                    self.screens[self.currentScreenIndex]()
                else:
                    self.engine.changeScene("mainMenu")

    def render(self):

        self.engine.screen.fill(BLACK)

        if self.preBlackOutTimer < self.timeBeforeBlackOut:
            self.preBlackOutTimer += self.engine.clock.get_time()

            for img in self.images:
                self.engine.screen.blit(img["image"], img["position"])

            Scene.render(self)

        elif self.blackOutTimer < self.timeBetweenScreens:

            self.blackOutTimer += self.engine.clock.get_time()

        else:
            self.resetScreen()

            if self.currentScreenIndex < len(self.screens) - 1:
                self.currentScreenIndex += 1
                self.screens[self.currentScreenIndex]()
            else:
                self.engine.changeScene("mainMenu")







