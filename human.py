from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        while True: 
            self.user_input = input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, or 4 for Spock\n")
            if self.user_input in ["0","1", "2", "3", "4"]:
                break
            else:
                print("No matching entry. Choose again.")
        user_input_converted = int(self.user_input)
        self.random_gesture = self.gesture[user_input_converted]


        # 1. I want to display the list of gesture options to my user in the console
        # 2. Prompt my user for input to find out which gesture they want
        # 3. I want to take that input, match it to the gesture they want
        # 4. I want to find a way to store that chosen gesture




