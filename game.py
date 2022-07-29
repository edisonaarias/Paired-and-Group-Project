from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player1 = Human()
        self.player2 = None
        user_input = input("Enter 2 if there are two players, otherwise press enter: ")
        if(user_input == "2"):
            self.player2= Human()
        else:
            self.player2= AI()

    def run_game(self):
        self.display_welcome()
        self.rounds()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to RPSLS!")
        print("Rules are as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock,\nRock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors,\nScissors decapitates Lizard, and Lizard eats Paper")

    def rounds(self):
        while self.player1.score < 2 and self.player2.score < 2:
            self.player1.choose_gesture()
            self.player2.choose_gesture()
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
        
    def display_winner(self):
        if self.player1.score > self.player2.score:
            print(f"{self.player1} is the winner!")
        else:
            print(f"{self.player2} is the winner!")
