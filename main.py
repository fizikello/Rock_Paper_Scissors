from random import choice

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

        self.weapon = input("choose Rock or Paper or Scissors [r,p,s]: ")[0].lower()

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

    def next_round(self):

        self.player_1.choose()
        self.player_2.choose()
        self.check_result()

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
        return (f"round {self.round}\n{self.player_1.name}: {self.player_1.weapon}\n"
                f"{self.player_2.name}: {self.player_2.weapon}\n"
                f"The winner of this round is {self.round_winner}\n"
                f"Result: {self.player_1.name}: {self.player_1.score} - {self.player_2.name}: {self.player_2.score}\n")



if __name__ == "__main__":

    a = UserPlayer('Arek')


    ai = Computer("AI")

    game = Game(round_limit=1, player_1=a, player_2=ai)
    game.next_round()
    print(game)



