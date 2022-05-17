
from inspect import getsourcelines


class Player:
    def __init__(self):
        pass
    def gestures(self, rock, paper, scissors, lizard, spock):
        self.rock = rock > lizard and rock >scissors
        self.paper = paper > rock and paper > spock
        self.scissors = scissors > lizard and scissors > paper
        self.lizard = lizard > spock and lizard > paper
        self.spock = spock > rock and spock > scissors
        

    # def count_down(self):
    #     self.dual = "winner is best two out of three!"

    # def selection(self):

    # # def gesture selected(self):

    # 2 methods needed 
    # - gestures 
    # - method to allow user to choose gesture 