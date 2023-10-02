# This program uses a loop to displaya table
# showing the numbers 1 through 10
# and their squares

# Get the ending limit
print('This program displays a list of numbers')
print('and their squares.')
start = int(input('Enter the starting number: '))

# Get the ending limit
end = int(input('How high should I go? '))

# Pring the table headings
print()
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their square
for number in range(start,end + 1):
    square = number ** 2
    print(number, '\t', square)