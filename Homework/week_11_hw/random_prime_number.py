# question 2

import random

def random_gen():
        # Get a random number
        return random.randint(1, 1000)

def is_prime(num):
    for i in range(2, num):
        if(num % i) == 1:
            return "Prime number"
            break
        else:
            return "not prime"
            break


def main():
    # have user enter how many number to generate
    userInput = int(input("Enter how many numbers to check if prime: "))

    for i in range(userInput):
        num = random_gen()
        print(f'{num} is {is_prime(num)}')


# Call the main function
main()