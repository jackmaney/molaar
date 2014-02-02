from Game.Shared.GameConstants import *
from Game.Scene.Scene import Scene


class GameScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)
        self.engine.loadEnemies()

    def update(self):

        self.texts = []
        self.addText("Score: " + str(self.engine.score), (0, 0))
        self.addText("Health: " + str(self.engine.player.health), (0, 20))

        self.engine.player.update()
        self.engine.candies.update()

        candidateCandies = pygame.sprite.spritecollide(self.engine.player, self.engine.candies, False)
        for candy in candidateCandies:
            if self.engine.player.bodyRect().colliderect(candy.rect):
                self.engine.player.health -= candy.damage
                candy.kill()

                if self.engine.player.health <= 0:
                    self.engine.changeScene("gameOver")

            elif self.engine.player.isSwinging and self.engine.player.hammerHeadRect().colliderect(candy.rect):
                self.engine.score += 1
                self.engine.playSound("impact")
                candy.kill()

        if self.engine.timeKeeper.timer - self.engine.loadEnemyTimer >= TIME_BETWEEN_ENEMY_LOADS:
            self.engine.loadEnemies()
            self.engine.loadEnemyTimer = self.engine.timeKeeper.timer

    def render(self):
        Scene.render(self)

        self.engine.player.render()
        self.engine.candies.draw(self.engine.screen)

    def handleEvents(self, events):
        self.engine.player.handleEvents(events)


