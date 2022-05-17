from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player = Player("rock")
        self.ai = AI("paper")

    def run_game(self):
        pass
    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizzard, Spock")
    
    def display_rules(self):
        print("Winner will be the best two of 3 matches\nUse the number keys to enter your selection.")

    def round_phase(self):
        pass
        # while self.human.hand 

    def display_winner(self):
        pass