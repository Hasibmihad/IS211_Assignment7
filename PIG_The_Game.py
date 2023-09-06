import random


class Die:
    def roll(self):
        random.seed(0)
        return random.randint(1, 6)
    


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


    def addScore(self, roll_points):
        self.score += roll_points


class PigTheGame:
            