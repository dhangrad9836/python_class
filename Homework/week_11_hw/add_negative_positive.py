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
    return total + user_input


subsetsum = 0
def main():
    global subsetsum

    user_input = input(f'Enter a number between -10 through 10:\n '
                       f'Or enter N to quit')

    while user_input != 'n' or user_input !='N':
        for num in user_input:
            if ord(num) not in range(48, 58):
                print("Not a number")
                return
            else:
                pass

        int_num = int(num)
        added_value = add(subsetsum, int_num)
        #update the subsetsum total
        subsetsum = added_value
        #check if subsetsum is zero
        if subsetsum == 0:
            print(f'The total is zero')
        else:
            pass
        user_input = input(f'Enter a number between -10 through 10:\n '
                           f'Or enter N to quit')
# call main function
main()