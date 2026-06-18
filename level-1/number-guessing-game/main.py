# concepts: loops, randomness

import random

score_counter = 0

while True:
    secret = random.randint(1, 10)
    attempts = 5

    print("\nNew Game Started! You have 5 attempts.")

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret:
            print("Correct!")
            score_counter += 1
            break

        elif guess < secret:
            print("Too low")
        else:
            print("Too high")
        
        attempts -= 1
        print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"You lost! The number was {secret}")
        
    print(f"Score: {score_counter}")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

