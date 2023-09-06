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

    def __str__(self):
        return f"{self.name} ({self.points} points)"

class PigTheGame:
    def __init__(self, players):
        self.players = [Player(player_name) for player_name in players]
        self.currentPlayerIndex = 0
        self.die = Die()


    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"{current_player.name}'s turn.")        