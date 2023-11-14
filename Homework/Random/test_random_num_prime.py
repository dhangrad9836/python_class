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
    #have user enter a number and the program will generate that many random numbers
    # the random numbers will be checked to see if they are prime or not
    userInput = input(("Enter a number to generate that many random numbers.\n"
                 "The program will validate if those numbers are prime or not."))
    while userInput != '0':

        for num in userInput:
            if ord(num) not in range(48, 58):
                print("Not a number")
                break
            else:
                pass

            if num == '0':
                break
            else:
                num = int(num)
                for i in range(num):
                    rand_num = random_gen()
                    print(f'{rand_num} is {is_prime(rand_num)}')

                userInput = input(("Enter another number to try again or 0 to quit: "))

main()