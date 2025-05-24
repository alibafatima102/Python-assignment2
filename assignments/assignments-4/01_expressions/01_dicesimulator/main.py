"""
Program: dicesimulator
----------------------
Simulates rolling two dice, three times. Prints
the results of each die roll. Demonstrates variable scope.
"""

import random

# Constant: Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Shows that die1 and die2 are local to this function.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    # Local variable die1 in main
    die1 = 10
    print("die1 in main() starts as:", die1)

    # Call the dice rolling function three times
    roll_dice()
    roll_dice()
    roll_dice()

    # Show that die1 in main has not changed
    print("die1 in main() is:", die1)

# Required to call the main function
if __name__ == '__main__':
    main()
