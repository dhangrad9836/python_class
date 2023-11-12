# 5. Write a program that asks the user to input an integer value for a variable called points.
# Write an if-else statement that checks whether the points variable is outside the range of 9 to 51.
# If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it should display “Valid points.”

# Ask user to enter in integer value
points = int(input('Enter an integer to check if it\'s in a certain range of numbers: '))

# Validate if the points variable is within a range of 9 to 51
if((points < 9) or (points > 51)):
    print("Invalid points")
else:
    print("Valid points")