from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.display_welcome()

    def run_game(self):
        self.player_selection()
        self.rounds()
        self.display_winner()

    def player_selection(self):
        user_input = input("Enter 2 if there are two players, otherwise press enter: ")
        self.player1 = Human(input("Enter player 1 name: "))
        self.player2 = None
        if(user_input == "2"):
            self.player2= Human(input("Enter player 2 name: "))
        else:
            self.player2= AI("The Computer")


    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!\n")
        print("Each match will be the best of three games!\nUse the number keys to enter your selection!\n\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\n\n")

    def rounds(self):
        while self.player1.score < 2 and self.player2.score < 2:
            self.player2.choose_gesture()
            self.player1.choose_gesture()
            if self.player1.random_gesture == "rock" and (self.player2.random_gesture == "paper" or self.player2.random_gesture == "spock"):
                self.player2.score += 1
            elif self.player1.random_gesture == "paper" and (self.player2.random_gesture == "scissors" or self.player2.random_gesture == "lizard"):
                self.player2.score += 1
            elif self.player1.random_gesture == "scissors" and (self.player2.random_gesture == "spock" or self.player2.random_gesture == "rock"):
                self.player2.score += 1
            elif self.player1.random_gesture == "lizard" and (self.player2.random_gesture == "scissors" or self.player2.random_gesture == "rock"):
                self.player2.score += 1
            elif self.player1.random_gesture == "spock" and (self.player2.random_gesture == "paper" or self.player2.random_gesture == "lizard"):
                self.player2.score += 1
            elif self.player2.random_gesture == "rock" and (self.player1.random_gesture == "paper" or self.player1.random_gesture == "spock"):
                self.player1.score += 1
            elif self.player2.random_gesture == "paper" and (self.player1.random_gesture == "scissors" or self.player1.random_gesture == "lizard"):
                self.player1.score += 1
            elif self.player2.random_gesture == "scissors" and (self.player1.random_gesture == "spock" or self.player1.random_gesture == "rock"):
                self.player1.score += 1
            elif self.player2.random_gesture == "lizard" and (self.player1.random_gesture == "scissors" or self.player1.random_gesture == "rock"):
                self.player1.score += 1
            elif self.player2.random_gesture == "spock" and (self.player1.random_gesture == "paper" or self.player1.random_gesture == "lizard"):
                self.player1.score += 1
            else:
                print("It's a tie. Play again.")
    def display_winner(self):
        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} is the winner!")
        else:
            print(f"{self.player2.name} outsmarted you!")
