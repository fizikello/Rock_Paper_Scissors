from random import choice
from tabnanny import check


class Player():

    def __init__(self, name):

        self.score = 0
        self.name = name
        self.weapon = None

    def choose(self, weapon):

        self.weapon = weapon

    def score_up(self):
        self.score += 1


    def __str__(self):
        return f"{self.name}: {self.weapon}"



class UserPlayer(Player):

    def __init__(self, name):

        super().__init__(name)

    def choose(self):

        try:
            self.weapon = input(f"{self.name}, please choose Rock or Paper or Scissors [r,p,s]: ")[0].lower()
        except IndexError:
            self.weapon = input("Please choose Rock or Paper or Scissors [r,p,s]: ")[0].lower()

class Computer(Player):
    def __init__(self, name):

        super().__init__(name)

    def choose(self):

        self.weapon = choice("rps")

class Game():

    def __init__(self, round_limit, player_1, player_2):

        self.round = 0
        self.round_limit = round_limit
        self.player_1 = player_1
        self.player_2 = player_2
        self.round_winner = None
        self.winner = None

    def next_round(self):

        self.round += 1
        print(f"round {self.round}")
        self.player_1.choose()
        self.player_2.choose()
        self.check_result()

    def check_final_result(self):

        if self.player_1.score > self.player_2.score:
            self.winner = self.player_1.name
        elif self.player_2.score > self.player_1.score:
            self.winner = self.player_2.name
        else:
            self.winner = None

    def play(self):

        while self.round < self.round_limit:
            self.next_round()
            print(self.__str__())

        self.check_final_result()
        print(f"\nCongratulations!\nThe winner is {self.winner}!")


    def check_result(self):

        if (self.player_1.weapon == 's' and self.player_2.weapon == 'p'
                or self.player_1.weapon == 'p' and self.player_2.weapon == 'r'
                or self.player_1.weapon == 'r' and self.player_2.weapon == 's'):
            self.player_1.score_up()
            self.round_winner = self.player_1.name
        elif (self.player_2.weapon == 's' and self.player_1.weapon == 'p'
                or self.player_2.weapon == 'p' and self.player_1.weapon == 'r'
                or self.player_2.weapon == 'r' and self.player_1.weapon == 's'):
            self.player_2.score_up()
            self.round_winner = self.player_2.name
        else:
            self.round_winner = None

    def __str__(self):
        return (f"{self.player_1.name}: {self.player_1.weapon}\n"
                f"{self.player_2.name}: {self.player_2.weapon}\n"
                f"The winner of this round is {self.round_winner}\n"
                f"Result: {self.player_1.name} {self.player_1.score} - {self.player_2.score} {self.player_2.name}\n")



if __name__ == "__main__":

    player = UserPlayer('Lewis')
    ai = Computer("AI")
    game = Game(round_limit=3, player_1=player, player_2=ai)
    game.play()



