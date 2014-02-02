from Game.Shared.GameConstants import *
from random import randint, random


class TimeKeeper(object):
    def __init__(self, engine):
        self.engine = engine
        self.timer = 0

    def getMinKey(self, thresholds):

        futureKeys = [time for time in thresholds if time >= self.timer]

        if len(futureKeys) == 0:
            return max(thresholds.keys())
        else:
            return min(futureKeys)

    def numCandies(self):

        return MAX_CANDY_THRESHOLDS[self.getMinKey(MAX_CANDY_THRESHOLDS)]

    def candyDamage(self):

        minKey = self.getMinKey(CANDY_DAMAGE_THRESHOLDS)

        return randint(CANDY_DAMAGE_THRESHOLDS[minKey]["min"], CANDY_DAMAGE_THRESHOLDS[minKey]["max"])

    def candySpeed(self):

        minKey = self.getMinKey(CANDY_SPEED_THRESHOLDS)

        return randint(CANDY_SPEED_THRESHOLDS[minKey]["min"], CANDY_SPEED_THRESHOLDS[minKey]["max"])

    def isCandyASeeker(self):

        minKey = self.getMinKey(CANDY_SEEKER_PROBABILITY_THRESHOLDS)

        return random() <= CANDY_SEEKER_PROBABILITY_THRESHOLDS[minKey]