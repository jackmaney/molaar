from Game.Shared.GameConstants import *
from Game.Scene.Scene import Scene
import pygame


class GameScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)

        self.engine.timeKeeper.resetTimer()
        self.engine.loadEnemies()
        pygame.mixer.init()

        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load(GAME_MUSIC_FILE)
        pygame.mixer.music.play(loops=-1)

    def update(self):

        self.texts = []
        self.addText("Score: " + str(self.engine.score), (0, 0))
        self.addText("Health: " + str(self.engine.player.health), (0, 20))
        self.addText("Time: " + self.engine.msToHMS(self.engine.timeKeeper.timer), (0, 40))

        self.engine.player.update()
        self.engine.toothbrushes.update()
        self.engine.candies.update()

        for brush in self.engine.toothbrushes:
            if self.engine.player.bodyRect().colliderect(brush.rect):
                self.engine.playSound("toothbrush")
                brush.kill()
                self.engine.player.health += HEALTH_REGAINED_FROM_TOOTHBRUSH
                if self.engine.player.health > 100:
                    self.engine.player.health = 100

        candidateCandies = pygame.sprite.spritecollide(self.engine.player, self.engine.candies, False)
        for candy in candidateCandies:
            if self.engine.player.bodyRect().colliderect(candy.rect):
                self.engine.player.health -= candy.damage
                candy.kill()

                if self.engine.player.health <= 0:
                    pygame.mixer.music.stop()
                    self.engine.changeScene("gameOver")

            elif self.engine.player.isSwinging and self.engine.player.hammerHeadRect().colliderect(candy.rect):
                self.engine.player.numCandiesCrushed += 1
                if candy.isSeeker:
                    self.engine.score += 2
                else:
                    self.engine.score += 1
                self.engine.playSound("impact")
                candy.kill()

        if self.engine.timeKeeper.timer - self.engine.loadEnemyTimer >= TIME_BETWEEN_ENEMY_LOADS:
            self.engine.loadEnemies()
            self.engine.loadEnemyTimer = self.engine.timeKeeper.timer

        if self.engine.timeKeeper.timer - self.engine.loadToothbrushTimer >= TIME_BETWEEN_TOOTHBRUSH_SPAWNS:
            self.engine.loadToothbrushes()
            self.engine.loadToothbrushTimer = self.engine.timeKeeper.timer

    def render(self):
        Scene.render(self)

        self.engine.player.render()
        self.engine.toothbrushes.draw(self.engine.screen)
        self.engine.candies.draw(self.engine.screen)

    def handleEvents(self, events):
        self.engine.player.handleEvents(events)


