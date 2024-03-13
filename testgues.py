# Author : Manoj G
# Date : 15-02-2024
# Batch : 3:30 - 5:30
# Description : Program to guess a random number in a set number of attempts

import random

max_attempts = 5
secret_number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {1} and {50}.")
print("You have", max_attempts, "attempts to guess it.")

attempts = 0

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try guessing higher.")
    elif guess > secret_number:
        print("Too high! Try guessing lower.")
    else:
        print("Congratulations! You guessed the number correctly!")
        print(f"It took you {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct number was {secret_number}")
