from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.random_gesture = random.choice[self.gesture]

    def random_selection(self):
        pass

    #TODO: override the choose_gesture method
