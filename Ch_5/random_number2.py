# This program displays 5 random numbers
# in the range of 1 through 100.
import random

def main():
    for count in range(5):
        # Get a random number
        number = random.randint(1, 100)

        # Display the number
        print(f'Number {count + 1} is {number}.')

# Call the main function
main()