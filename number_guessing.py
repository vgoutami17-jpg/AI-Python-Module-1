# Number Guessing Game

import random

secret_number = random.randint(1, 50)
attempts = 7

print("Guess the number between 1 and 50.")
print("You have", attempts, "attempts.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print("Game over. The number was:", secret_number)
