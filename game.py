from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player = Human()
        self.ai = AI()

    def run_game(self):
        print("Hello World. Welcome to RPSLS")
        self.player.choose_gesture()

    def display_welcome(self):
        pass

    def rounds(self):
        pass

    def display_winner(self):
        pass
