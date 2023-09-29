# 3. Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

# Ask user to enter the total bill for the meal and convert input to float
bill_for_meal = float(input('Enter the total amount for your meal purchased: '))

# Constants for eighteen percent tip and seven percent sales tax
EIGHTEEN_PERCENT_TIP = 0.18
SEVEN_PERCENT_TAX = 0.07

# calculate the sales tax amount
sales_tax = bill_for_meal * SEVEN_PERCENT_TAX
#print(sales_tax)

# calculate the tip amount
tip_amount = (bill_for_meal + sales_tax) * EIGHTEEN_PERCENT_TIP
print(f'tip amount: {tip_amount}')

# Calculate the total amount with the tip and sales tax
total_amount = bill_for_meal + tip_amount + sales_tax
#print(f'Total amount {total_amount}')

# Display the tip amount
print(f'The tip amount is : ${tip_amount:.2f}')

# Display the sales tax amount.
print(f'The sales tax is : ${sales_tax:.2f}')

# Display the total amount of the bill
print(f'The total amount is : ${total_amount:.2f}')