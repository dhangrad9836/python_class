# question 3...
import random
# function that generates a number between 1 through 1000
def random_gen():
        # Get a random number and return to calling function
        return random.randint(1, 1000)

# check_guess function checks users guess against the random number
# function will tell you if you guessed too high, too low or you guessed correctly
def check_guess(user_num, rand_num):
    rand_x = rand_num
    user_y = user_num
    count = 0
    while user_y != 00:
        if user_y == 00:
            return 'Game over'
        elif user_y > rand_x:
            print('Too high')
            user_y = int((input('Try again:')))
        elif user_y < rand_x:
            print('Too low')
            user_y = int((input('Try again:')))
            count += 1
        elif user_y == rand_x:
            return f'You guessed correctly'

def main():
    #have user enter a number and the program will generate that many random numbers
    # the random numbers will be checked to see if they are prime or not
    userInput = input(("Guess a number between 1 - 1000.\n"
                 "I will tell you whether you are higher or lower: \n"
                 "Enter 00 to quit: "))
    while userInput != '00':

        #validate tha the user enters a number
        for num in userInput:
            if ord(num) not in range(48, 58):
                print("Not a number")
                break
            else:
                pass

        if num == '00':
            break
        else:
            user_num = int(num)
            rand_num = random_gen()
            guess_checker = check_guess(user_num, rand_num)
        print(f'{guess_checker}')



main()