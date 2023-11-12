# 7. The date June 10, 1960, is special because when it is written in the following format, the
# month times the day equals the year:
# 6/10/60
# Write a program that asks the user to enter a month (in numeric form), a day, and a two-
# digit year. The program should then determine whether the month times the day equals the
# year. If so, it should display a message saying the date is magic. Otherwise, it should display
# a message saying the date is not magic.

# Ask user to input month and store as int
month_number = int(input('Enter a number in numeric form between (1 - 12) for the month: '))

# Ask user to input a number for the day and store as an int
day_number = int(input('Enter a number in numeric form between (1 - 31) for the day: '))

# Ask user to input a two digit number for the year and store as an int
year_number = int(input('Enter a two digit number for the year (ie: 1970 enter 70): '))

# validate if the date is a magic date
# if the product of month_number and day_number is equal to the year_number
# then it's a magic date
if((month_number * day_number) == year_number):
    print(f'The date {month_number}/{day_number}/{year_number} is magic')
else:
    print(f'The date {month_number}/{day_number}/{year_number} is not magic')