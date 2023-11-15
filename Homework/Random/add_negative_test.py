# question 4...
#4. Write a program that asks user to input negative and positive integers between -10 and 10. The program will
# add up the numbers and terminate when the sum of the values becomes zero. The program should contain
# the following functions:
# add()    : add up the values
# main(): the function where the program execution should begin and end.


# global variable subsetsum
#subsetsum = 0
# add function that adds user inputs
def add(number_list):
    add_total = 0

    for x in number_list:
        add_total += x
    return add_total


subsetsum = 0
def main():
    global subsetsum

    user_input = input(f'Enter a number between -10 through 10\n '
                       f'Or enter 000 to quit: ')

    number_list = list()

    while user_input != '000':
        for num in user_input:
            if ord(num) not in range(48, 58):
                print("Not a number")
                return
            else:
                pass

        number_list.append(int(user_input))
        # int_num = int(num)
        added_value = add(number_list)
        subsetsum = added_value
        print(subsetsum)
        if subsetsum == 0:
            print('Total is zero')
        else:

            user_input = input(f'Enter a number between -10 through 10\n '
                               f'Or enter 000 to quit: ')
        #update the subsetsum total
        # subsetsum = added_value
        # #check if subsetsum is zero
        # if subsetsum == 0:
        #     print(f'The total is zero')
        # else:
        #     pass
        # user_input = input(f'Enter a number between -10 through 10\n '
        #                    f'Or enter N to quit: ')
# call main function
main()