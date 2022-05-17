
class Player:
<<<<<<< HEAD
    def __init__(self, gesture):
        self.gesture = ["rock, paper, scissors, lizard, spock"]
        self.attack = rock > lizard and rock >scissors and paper > rock and paper > spock and scissors > lizard and scissors > paper and lizard > spock and lizard > paper and spock > rock and spock > scissors
        
        # TODO: just a single instance variable - a List of gestures (string)

    def choose_gestures(self):
        pass
        

=======
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
>>>>>>> 22a09aa21047493ea902df519368106d8d213199

    # def gesture selected(self):