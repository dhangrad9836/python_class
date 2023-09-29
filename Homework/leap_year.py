# The month of February normally has 28 days. But if it is a leap year, February has 29 days.
# Write a program that asks the user to enter a year. The program should then display the
# number of days in February that year. Use the following criteria to identify leap years:
# a Determine whether the year is divisible by 100. If it is, then it is a leap year if and only
# if it is also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
# b. If the year is not divisible by 100, then it is a leap year if and only if it is divisible by 4.
# For example, 2008 is a leap year, but 2009 is not.

# Ask user to enter a year to determine if it's a leap year
year_entered = int(input('Enter a year to find out if it\'s a leap year: '))

# validate if the year is divisible by 100
if((year_entered % 100) == 0):
    # validate if the year is divisible by 400
    if((year_entered % 400) == 0):
        # if both checks are true then it's a leap year with 29 days
        print(f'February of {year_entered} has 29 days in it')
    else:
        # if not divisible by 400 then that year has 28 days
        print(f'February of {year_entered} has 28 days in it')
# validate if the year is not divisible by 100 but divisible by 4
elif((year_entered % 4) == 0):
    # if divisible by 4 then that year is a leap year with 29 days
    print(f'February of {year_entered} has 29 days in it')
else:
    # if not divisible by 4 then that year has 28 days
    print(f'February of {year_entered} has 28 days in it')