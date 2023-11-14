# question 3

#import random package
import random

# function that generates a number between 1 through 1000
def random_gen():
        # Get a random number
        return random.randint(1, 1000)

# function to check the users guess
def check_guess(user_guess_number):
    # store the number of user guesses in count variable
    count = 1
    # store a random number in random_number variable
    random_number = random_gen()
    while user_guess_number != random_number:
        if user_guess_number > random_number:
            print("Too high, try again")
        elif user_guess_number < random_number:
            print("Too low, try again")
        count += 1
    if user_guess_number == random_number:
            print(f'You guess the correct number after {count} guesses')
    else:
        pass
# main function
def main():

    #Have user guess a nuber between 1 through 1000
    user_guess = int(input(f'Guess a number between 1 through 1000: '))

    # check if users guesses the right number
    check_guess(user_guess)

#call main function
main()