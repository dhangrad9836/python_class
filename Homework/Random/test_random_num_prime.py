# question 2...
import random

#random_gen function generates a single random number from 1 through 1000
def random_gen():
        # Get a random number
        return random.randint(1, 1000)

#is_prime function tests wether the random numbers are prime or not
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
                 "The program will validate if those numbers are prime or not.: "))
    while userInput != '0':

        for num in userInput:
            #validate the users input is a number via the string input to ascii values
            if ord(num) not in range(48, 58):
                print("Not a number")
                break
            else:
                pass
            #if user selects '0' user wants to quit
            if num == '0':
                break
            else:
                #store the userInput into num variable
                num = int(userInput)
                #take the userInput and pass in the for loop which will callthe random_gen function
                #this will generate that many numbers and then it wll pass individually
                #each random number inside the is_prime function to test if each are prime or not
                for i in range(num):
                    rand_num = random_gen()
                    print(f'{rand_num} is {is_prime(rand_num)}')
                #ask the user to enter another number or 0 to quit
                userInput = input(("Enter another number to try again or 0 to quit: "))

main()