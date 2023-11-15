# question 3...
import random
# function that generates a number between 1 through 1000
def random_gen():
        # Get a random number
        return random.randint(1, 1000)

def check_guess(user_num, rand_num):
    x = rand_num
    y = user_num
    count = 0
    while y != 00:
        if y == 00:
            return 'Game over'
        elif y > x:
            print('Too high')
            y = int((input('Try again:')))
        elif y < x:
            print('Too low')
            y = int((input('Try again:')))
            count += 1
        elif y == x:
            return f'You guessed correctly'

def main():
    #have user enter a number and the program will generate that many random numbers
    # the random numbers will be checked to see if they are prime or not
    userInput = input(("Guess a number between 1 - 1000.\n"
                 "I will tell you whether you are higher or lower: \n"
                 "Enter 00 to quit: "))

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