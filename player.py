
class Player:
    def __init__(self, name, players):
        self.name = name 
        self.players = players                                                      # need to make sure that self.players can be used to ask user, how many are playing.
        
    # we believe hand will have rock,paper scissors,lizard, and spock as parameters.

    def hand(self): 
        self.rock -= self.attack_power()
        self.rock = "rock"
        self.paper = "paper"
        self.scissors = "scissors"    
        self.lizard = "lizard" 
        self.spock = "spock"

    def count_down(self):
        self.dual = "winner is best two out of three!"

    def selection(self):

    # def gesture selected(self):