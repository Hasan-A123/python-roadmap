# ====================================
# Project 8 - Rock Paper Scissors
# Python Roadmap
# Play Rock Paper Scissors against the computer
# ====================================

import random


def main():

    # Scoreboard variables
    # These keep track of the results across multiple rounds
    player_wins = 0
    computer_wins = 0
    draws = 0

    # Keeps track of how many rounds have been played
    round_number = 0

    # Store all valid choices in a list
    choices = ["rock", "paper", "scissors"]

    # Main game loop
    # This repeats the game until the player chooses to stop
    while True:

        print("\n=== ROCK PAPER SCISSORS ===")

        # Increase the round number by 1 at the start of each round
        round_number += 1
        print(f"\n=== ROUND {round_number} ===")

        # Ask the player to choose an option
        # .lower() converts the input to lowercase
        # so "ROCK" and "Rock" become "rock"
        user_choice = input(
            "Choose between: rock, paper, or scissors: "
        ).lower()

        # Check whether the player's choice exists in the choices list
        if user_choice not in choices:
            print("Invalid choice. Select choices from the list")
            return

        # Randomly choose one option for the computer
        computer_choice = random.choice(choices)

        # Display both choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Check all situations where the player wins
        #
        # Rock beats scissors
        # Scissors beats paper
        # Paper beats rock
        if (
            (user_choice == "rock" and computer_choice == "scissors")
            or
            (user_choice == "scissors" and computer_choice == "paper")
            or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win")

            # Increase the player's score by 1
            player_wins += 1

        # If both choices are the same, the round is a draw
        elif user_choice == computer_choice:
            print("It's a draw!")

            # Increase the draw count by 1
            draws += 1

        # If the player did not win and it was not a draw,
        # the computer must have won
        else:
            print("Computer wins!")

            # Increase the computer's score by 1
            computer_wins += 1

        # Display the current scoreboard after each round
        print("\n=== SCOREBOARD ===")
        print(f"Player Wins: {player_wins}")
        print(f"Computer Wins: {computer_wins}")
        print(f"Draws: {draws}")

        # Ask the player whether they want another round
        play_again = input(
            "\nDo you want to play again? (yes/no): "
        ).lower()

        # Keep asking until the player enters a valid answer
        while play_again not in ("yes", "no"):
            print("Please enter yes or no")

            play_again = input(
                "\nDo you want to play again? (yes/no): "
            ).lower()

        # End the main game loop if the player chooses "no"
        if play_again == "no":
            break

    print("\nThanks for playing")


# Run the program only when this file
# is executed directly.
if __name__ == "__main__":
    main()