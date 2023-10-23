# Variable to control the loop
calculate_two_numbers = 'y'

# Have user input two numbers to calculate the sum to the two numbers
while calculate_two_numbers == 'y':
    # users input for value_one
    value_one = int(input('Enter your first number: '))
    # users input for value_two
    value_two = int(input('Enter your second number: '))

    #perform the addition of the two inputed numbers
    sum_of_two_numbers = value_one + value_two

    # print the sum of the two numbers
    print(f'The sum of {value_one} + {value_two} is: {sum_of_two_numbers}')

    # ask user if he/she wants to perform the operation again
    calculate_two_numbers = input('Do you want to perform the operation again?\n'
                                  'Enter y to continue or n to stop: ')