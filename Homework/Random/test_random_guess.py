# question 3
import random
# function that generates a number between 1 through 1000
def random_gen():
        # Get a random number
        return random.randint(1, 1000)

def main():
    #have user enter a number and the program will generate that many random numbers
    # the random numbers will be checked to see if they are prime or not
    userInput = input(("I'll generate a number and you try to guess it.\n"
                 "I will tell you higher or lower."))

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
                print(f'')

main()