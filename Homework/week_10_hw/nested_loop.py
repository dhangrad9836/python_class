# Have user enter a number to display a pattern
NUM_OF_ROWS = int(input('Enter a number to display a pattern with # symbols: '))

# Validate the user enters a number greater than zero
while NUM_OF_ROWS <= 0:
    # alert to user that number entered is invalid
    print('Your number is invalid: ')
    # have user re-enter a number greater than zero
    NUM_OF_ROWS = int(input('Enter a number greater than zero: '))

# nested for loop to print out rows and columns of # symbols
# the outer for loop takes in the user input for the number of rows
for row in range(NUM_OF_ROWS):
    # each time the loop runs a new row will print out a '#' symbol and
    # suppress printing a newline with end=''
    print('#', end='')
    # the inner loop prints out a space for each inner loop iteration
    # ie: if col = 4 than the inner loop will loop 4 times and each iteration
    # will print out a space for each column of that row and suppress a new line with end=''
    for col in range(row):
        print(' ', end='')
    # now the inner loop breaks out and back into the outer loop and will print
    # a '#' symbol at the end of the row
    print('#')


