# This is a program that simulates a lottery.
# The program has a list of seven numbers that represent a lottery ticket.
# It then generates seven random numbers.
# After comparing the two sets of numbers, the program outputs a prize based on the number of matches:
# £20 for three matching numbers
# £40 for four matching numbers
# £100 for five matching numbers
# £10000 for six matching numbers
# £1000000 for seven matching numbers

# Import random module
import random

# Define range of lottery numbers
lottery_nums = range(1, 20)

# Find out if user wants to play
choose_lottery = input('Would you to play the lottery? ').strip().lower()

# If user wants to play, first generate and print their numbers
if choose_lottery == 'y' or choose_lottery == 'yes':
    player_ticket = random.sample(lottery_nums, k=7)
    print(f'Your numbers are: {player_ticket}')

    # Then generate and print winning_ticket numbers
    winning_ticket = random.sample(lottery_nums, k=7)
    print(f'The winning numbers are: {winning_ticket}')

    # Then compare player numbers and winning numbers to create list of matching numbers
    matching_nums = list(set(player_ticket).intersection(set(winning_ticket)))

    # Then print winnings, depending on length of the list of matching numbers
    if len(matching_nums) == 3:
        print(f'You have 3 matching numbers!  You win £20.')
    elif len(matching_nums) == 4:
        print(f'You have 4 matching numbers!  You win £40.')
    elif len(matching_nums) == 5:
        print(f'You have 5 matching numbers!  You win £100.')
    elif len(matching_nums) == 6:
        print(f'You have 6 matching numbers!  You win £10000.')
    elif len(matching_nums) == 7:
        print(f'You have 7 matching numbers!  You win £1000000.')
    else:
        print('Sorry, you didn\'t win this time!')
# If user doesn't want to play, then print message
else:
    print('Ok, maybe next time!')


