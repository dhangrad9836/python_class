#4. Write a program that asks user to input negative and positive integers between -10 and 10. The program will
# add up the numbers and terminate when the sum of the values becomes zero. The program should contain
# the following functions:
# add()    : add up the values
# main(): the function where the program execution should begin and end.


# global variable subsetsum
subsetsum = 0
# add function that adds user inputs
def add(user_input):
    global subsetsum
    total = subsetsum + user_input
    return total

# main function
def main():
    total = 0
    # have user enter negative and positive integers between -10 and 10
    users_integer_input = int(input('Enter negative and positive integers between -10 and 10: '))

    while users_integer_input != :
        total += add(users_integer_input)



        #ask user if he/she wants to do it again
        again = input('Do you want to do this again? Enter Y for yes')




# call main function
main()