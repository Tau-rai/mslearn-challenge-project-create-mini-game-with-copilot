# build a python console minigame the rules are simple: Rock beats Scissors, Scissors beats Paper, Paper beats Rock and if both players choose the same, it is a tie.

import random

def get_user_choice():
    """Get the user's choice."""
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Get the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}\n")
        result = determine_winner(user_choice, computer_choice)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() not in ["yes", "y"]:
            print(f"Final score: You - {user_score}, Computer - {computer_score}")
            break

if __name__ == "__main__":
    play_game()
