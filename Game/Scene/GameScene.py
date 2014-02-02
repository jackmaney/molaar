from Game.Shared.GameConstants import *
from Game.Scene.Scene import Scene

class GameScene(Scene):
    def __init__(self, engine):
        Scene.__init__(self, engine)
        self.engine.loadEnemies()

    def update(self):

        self.engine.player.update()
        self.engine.candies.update()

        candidateCandies = pygame.sprite.spritecollide(self.engine.player, self.engine.candies, False)
        for candy in candidateCandies:
            if self.engine.player.bodyRect().colliderect(candy.rect):
                print "Body Blow!"
            elif self.engine.player.isSwinging and self.engine.player.hammerHeadRect().colliderect(candy.rect):
                #print "Hammer hit!"
                self.engine.playSound("impact")
                candy.kill()
                #print len(self.candies)

    def render(self):
        Scene.render(self)

        self.engine.player.render()
        self.engine.candies.draw(self.engine.screen)

    def handleEvents(self, events):
        self.engine.player.handleEvents(events)


