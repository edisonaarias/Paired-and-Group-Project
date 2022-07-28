from player import Player

class Human(Player):
    def __init__(self):
        self.player_name = input()
        super().__init__()

    #TODO: override the choose_gesture method
    def choose_gesture(self):
        print(self.gesture)
        self.user_input = input("Choose 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, or 4 for Spock\n")
        self.gesture = self.user_input 
        print(f"{self.player_name} {self.user_input}")


        # 1. I want to display the list of gesture options to my user in the console
        # 2. Prompt my user for input to find out which gesture they want
        # 3. I want to take that input, match it to the gesture they want
        # 4. I want to find a way to store that chosen gesture

# my_human = Human()
# my_human.choose_gesture()




