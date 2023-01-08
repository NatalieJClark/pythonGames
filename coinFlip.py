# This program uses random to simulate a coin flip.
# If the random coin flip matches the choice input by the user then they win
# Otherwise if the random coin flip does not match the choice input by the user then they lose

# Import random library
import random


# Define function to return coin flip result
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = "heads"
    else:
        side = "tails"
    return side

# Request user choice, remove spaces and convert to lower case
choice = input("heads or tails: ").strip().lower()

# Call flip_coin() function and print result
result = flip_coin()

print(f"The coin landed on {result}")

# Compare user choice and coin flip and print outcome
if choice == result:
    print(f"You win!")
else:
    print(f"Oh dear, you lose!")