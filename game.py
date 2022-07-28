from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player = Human()
        self.ai = AI()

    def run_game(self):
        self.display_welcome()
        self.rounds()

    def display_welcome(self):
        print("Welcome to RPSLS!")
        print("Rules are as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock,\nRock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors,\nScissors decapitates Lizard, and Lizard eats Paper")


    def rounds(self):
        self.player.choose_gesture()

    def display_winner(self):
        pass
