import random 
from player import Player

class AI(Player):
    def __init__(self):
        self.name = "Robot"
        super().__init__()

    def choose_gesture(self):
        self.random_gesture = random.choice[self.gesture]

    def 

    #TODO: override the choose_gesture method