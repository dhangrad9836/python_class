# This program simulates 10 tosses of a coin
import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Simulate the coin toss.
        # remember inside the randomint(heads = 1, tails = 2)
        # so the random number will be either 1 or 2 and if it's == to heads which is 1
        if random.randint(HEADS, TAILS) == HEADS:

            print(('Heads'))
        else:

            print('Tails')

# Call main funciton
main()