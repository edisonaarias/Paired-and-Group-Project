from unicodedata import name
from player import Player
import random

class AI(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        self.random_gesture = random.choice(self.gesture)

       ## random_number = random.randint(5)
       ## self.random_gesture = self.gesture[random_number]

    def random_selection(self):
        pass

