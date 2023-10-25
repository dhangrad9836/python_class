# We need to have a way to multiply from 1 to n
# where n is the user input number or the factorial

# Have the user input a non-negative number to find its factorial
factorial_number = int(input('Enter a non-negative number to calculate the factorial: '))

# while loop to check if user input is a non-negative number
while factorial_number < 0:
    # display error message to user
    print('Your number cannot be negative')
    # have user re-enter another number and store it in current factorial_number variable
    factorial_number = int(input('Enter a non-negative number: '))

# total variable to keep running total
total = 1
# use for loop to calculate the factorial of users input
for number in range(factorial_number):
    # calculate the factorial and store it in the total variable
    total *= (number + 1)
    #print(total)
print(total)