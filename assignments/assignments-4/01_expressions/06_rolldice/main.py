"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random  # For generating random numbers

NUM_SIDES = 6  # Number of sides on each die

def main():
    # Uncomment the next line to get reproducible results for debugging
    # random.seed(1)
    
    # Roll the dice
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)

    # Calculate the total of the two dice
    total = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

if __name__ == '__main__':
    main()
