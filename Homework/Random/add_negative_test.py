# question 4...

# global variable subsetsum
#subsetsum = 0
# add function that adds user inputs
def add(total, user_input):
    add_total = total + user_input
    return add_total


subsetsum = 0

def main():
    global subsetsum
    #have user enter a number between -10 through 10
    user_input = input(f'Enter a number between -10 through 10\n '
                       f'Or enter 000 to quit: ')
    #if user selects 000 program ends
    while user_input != '000':
        #check if user input is an int
        if type(user_input) == int:
            pass
            #validate if users input is between -10 and 10
            if int_num > -10 or int_num < 10:
                #if input is out of range re-run the program
                user_input = input(f'Enter a number between -10 through 10\n '
                                   f'Or enter 000 to quit: ')
            else:
                pass
        else:
            #if users input is not an int type re-run program
             user_input = input(f'Enter a number between -10 through 10\n '
                            f'Or enter 000 to quit: ')
        #once users input is valid convert input into int
        int_num = int(user_input)
        #call the add function and pass in the subsetsum running total and users input
        added_value = add(subsetsum, int_num)
        #update the subsetsum with the new total
        subsetsum = added_value
        #print(subsetsum)
        #if subsetsum is zero print out total is zero
        if subsetsum == 0:
            print('Total is zero')
            pass
        else:
            pass



# call main function
main()