# This program gets an item's original price and
# Calculates its sale price, with 20% discount

# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.2

# Calculate the sale price
sale_price = original_price - discount

# Display the sale price
print('The sale price is', sale_price)