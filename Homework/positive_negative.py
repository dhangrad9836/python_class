# 6. Write a program that asks the user to enter an integer. The program should display
# “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
# “Zero” if the number is equal to 0. The program should then display “Even” if the number
# is even, and “Odd” if the number is odd.

# Ask the user to enter an integer to validate if it's positive, negative, even, or odd
number_to_validate = int(input('Enter an integer to validate: '))

# Validate and print whether the user's input is positive, negative, or zero
if(number_to_validate > 0):
    print('Positive')
elif(number_to_validate < 0):
    print('Negative')
elif(number_to_validate == 0):
    print('Zero')

# validate if the user input is even or odd using modulus operator %
# if the result is 0 then it's even else it's odd
if(number_to_validate % 2 == 0):
    print('Even')
else:
    print('Odd')