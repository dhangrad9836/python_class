# question 4...
#4. Write a program that asks user to input negative and positive integers between -10 and 10. The program will
# add up the numbers and terminate when the sum of the values becomes zero. The program should contain
# the following functions:
# add()    : add up the values
# main(): the function where the program execution should begin and end.


# global variable subsetsum
#subsetsum = 0
# add function that adds user inputs
def add(total, user_input):
    add_total = total + user_input
    return add_total


subsetsum = 0
def main():
    global subsetsum

    user_input = input(f'Enter a number between -10 through 10\n '
                       f'Or enter 000 to quit: ')

    while user_input != '000':
        for num in user_input:
            if ord(num) not in range(48, 58):
                print("Not a number")
                return
            else:
                pass

        #pass/convert original user_input as int
        int_num = int(user_input)
        added_value = add(subsetsum, int_num)
        subsetsum = added_value
        print(subsetsum)
        if subsetsum == 0:
            print('Total is zero')
            pass
        else:
            pass

            user_input = input(f'Enter a number between -10 through 10\n '
                                f'Or enter 000 to quit: ')

# call main function
main()