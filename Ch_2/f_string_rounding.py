# This program demonstrates how a floating point
# number can be rounded
amount_due = 5000.0
montly_payment = amount_due /12.0
print(f'The monthly payment is {montly_payment:.2f}.')

# example of usint format-specifier for commas
number = 1234567.12345
print(f'{number:,}')

# now using both commas and to two decimal places...note that the comma seperator must be wriiten
# before or first then the precision .2f
print(f'${number:,.2f}')
print(f'{.5:.0%}')
print(f'${number:.2e}')
number2 = 123456.9875
print(f'The number is {50:10}')

print(f'Formatted number2 {number2:12.2f}')