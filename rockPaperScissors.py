# This program simulates rock, paper, scissors.

# Import random library
import random


# Define function to return opponent's random choice
def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = "rock"
    elif choice_number == 2:
        choice = "scissors"
    else:
        choice = "paper"

    return choice


# Request users choice, remove spaces and convert to lower case
my_choice = input("Choose rock, scissors or paper: ").strip().lower()

# Call random_choice() function to generate opponent's choice, and print output
opponent_choice = random_choice()

print(f"Your opponent chose {opponent_choice}")


# Compare user and opponent choices to decide and print outcome
if my_choice == opponent_choice:
    print("It\'s a draw!")
elif my_choice == "rock" and opponent_choice == "scissors":
    print("You win!")
elif my_choice == "paper" and opponent_choice == "scissors":
    print("You lose!")
elif my_choice == "paper" and opponent_choice == "rock":
    print("You win!")
elif my_choice == "scissors" and opponent_choice == "rock":
    print("You lose!")
elif my_choice == "rock" and opponent_choice == "paper":
    print("You lose!")
else:
    print("You win!")

