import random
class Die:
    def roll(self):
        random.seed(0)
        return random.randint(1, 6)