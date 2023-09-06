import random
import sys


class Dice:
    def roll(self):
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
        self.players = [Player(input(f"Enter Player {i + 1}'s name: ")) for i in range(num_players)]
        self.dice = Dice()
        self.current_player = 0

    """def is_game_over(self):
        for player in self.players:
            if player.score >= 10:
                return True
        return False
    
"""
    def change_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"{player.name}'s turn.")
        point=0
        while (True):
            roll = self.dice.roll()
            if roll == 1:
                    print(f"{player.name} rolled a 1 and lost his turn.")
                    point=0
                    str=player.__str__()
                    print(str)
                    break
                
            else :
                    #player.addScore(roll)
                    point+=roll
                    print(f"{player.name} rolled a {roll}")
                    pointstoshow=player.score+point
                    print (f"{player.name} scored {pointstoshow} points")
                    #str=player.__str__()
                    #print(str)
                    
                    if pointstoshow>=10:
                        break

                     
            ch=input("Press  'r'  to roll the dice, 'h' to hold : ")
            if ch.lower() == 'h':
                break
            elif ch.lower() == 'r':
                continue
            else : 
                print("\nGame Over!")
                sys.exit()
        player.score+=point  

        print(f"{player.name}'s turn is over. {player.name} scored {player.score}.")
        self.change_player()  

  

    def play(self):
        while all(player.score < 10 for player in self.players):
            self.play_turn()

        winners = [player for player in self.players if player.score >= 10]
        print("\nGame Over!")
        if len(winners) == 1:
            print(f"{winners[0].name} is the winner with {winners[0].score} points!")


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    game = PigTheGame(num_players)
    game.play()
