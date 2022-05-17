from human import Human
from ai import AI

class Game:
    def __init__(self):
        # self.player = Player("rock")
        self.ai = AI("paper")

    def run_game(self):
        self.display_welcome()
        self.rules()
        # self.round_phase()

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def rules(self):
        print("Each match will be best of three games!\nUse the number keys to enter your selection.")

    def round_phase(self):
        pass
        # while 
        #     print("Next round! First player to win twice is the winner.")

    def display_winner(self):
        print("Player has won!")

my_game = Game() 
my_game.run_game()