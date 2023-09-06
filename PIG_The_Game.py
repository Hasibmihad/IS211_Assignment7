import random
import sys


class Dice:
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
        return f"{self.name} ---- > ({self.score} points)"

class PigTheGame:
    def __init__(self, num_players):
        self.players = [Player(input(f"Enter Player {i + 1}'s name: ")) for i in range(num_players)]        self.currentPlayerIndex = 0
        self.dice = Dice()
        self.current_player = 0


    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"{player.name}'s turn.")
        print (player.__str__)
        ch=input("Press r to roll the dice, h to hold")
        if ch.lower()=='r':
            roll = self.dice.roll()
            if roll == 1:
                print(f"{player.name} rolled a 1 and lost his turn.")
                player.points = 0
            else :
                player.addScore(roll)
        elif ch.lower()=='h':   
                



   