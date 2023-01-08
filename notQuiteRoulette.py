# This program simulates a Roulette style game
# After generating a random number and colour:
# If the colour matches, the users keeps the amount that was bet
# If the number matches, the users wins double the amount that was bet
# If the colour and number matches, the users wins 100 times the amount that was bet
# When neither the colour or number matches the user wins 0

# Import random library
import random


# Define function to generate random colour
def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = "red"
    else:
        colour = "black"

    return colour

# Gather user data
bet = float(input("How much do you want to bet? (£) "))
colour_choice = input("Choose a colour (red or black) ").strip().lower()
number_choice = int(input("Choose a whole number between 1 and 100 "))

# Generate random number between 1 and 100, call random_colour() function and print outputs
roulette_number = random.randint(1, 100)
roulette_colour = colour()

print(f"The wheel landed on {roulette_number}, {roulette_colour}")

# Compare user data and random data and print outcome
win_colour = colour_choice == roulette_colour
win_number = number_choice == roulette_number

if win_colour:
    print(f"You keep your £{bet} bet")
elif win_number:
    print(f"You win £{2 * bet}")
elif win_colour and win_number:
    print(f"Congratulations!  You win £{100 * bet}")
else:
    print("Sorry, you win £0")
