# Author : Manoj G
# Date : 15-02-2024
# Batch : 3:30 - 5:30
# Description : Program to guess a random number in a set number of attempts

import random


class NumberGuessingGame:
    def __init__(self, max_attempts=5):
        # Initializing the game parameters to play the game
        self.max_attempts = max_attempts
        self.secret_number = random.randint(1, 50)

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between {1} and {50}.")
        print("You have", self.max_attempts, "attempts to guess it.")

        attempts = 0  # Initialize the attempt count
        # Start the game loop
        while attempts < self.max_attempts:
            guess = int(input("Enter your guess: "))
            # Increment the attempt count
            attempts += 1

            if guess < self.secret_number:
                print("Too low! Try guessing higher.")
            elif guess > self.secret_number:
                print("Too high! Try guessing lower.")
            else:
                print("Congratulations! You guessed the number correctly!")
                print(f"It took you {attempts} attempts.")
                return

        print(f"Sorry, you've used all your attempts. The correct number was {self.secret_number}")


# Creating an instance of the NumberGuessingGame class and play the game
game = NumberGuessingGame()
game.play()
