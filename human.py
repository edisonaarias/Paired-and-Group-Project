from player import Player

class Human(Player):
    def __init__(self):
        self.player_name = Human("")
        super().__init__()

    #TODO: override the choose_gesture method
    def choose_gesture(self):
        print(self.gesture)
        self.user_input = input("Choose 0 for Rock, Choose 1 for Paper, Choose 2 for Scissors, Choose 3 for Lizard, Choose 4 for Spock")
        self.gesture = self.user_input 
        print(f"Player 1 chose {self.user_input}")


        # 1. I want to display the list of gesture options to my user in the console
        # 2. Prompt my user for input to find out which gesture they want
        # 3. I want to take that input, match it to the gesture they want
        # 4. I want to find a way to store that chosen gesture

my_human = Human()
my_human.choose_gesture()




