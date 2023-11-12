# Serendipity Booksellers has a book club that awards points to its customers based on the
# number of books purchased each month. The points are awarded as follows:
# • If a customer purchases 0 books, he or she earns 0 points.
# • If a customer purchases 2 books, he or she earns 5 points.
# • If a customer purchases 4 books, he or she earns 15 points.
# • If a customer purchases 6 books, he or she earns 30 points.
# • If a customer purchases 8 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has pur-
# chased this month, then displays the number of points awarded

# Ask user to enter how many books (he/she) has purchased this month
books_purchased = int(input('Enter how many you have purchased this month: '))

# if books_purchased == 0 then 0 points are awarded
if(books_purchased == 0):
    print('You have earned 0 points.')
# if books_purchased == 2 then 5 points are awarded
elif(books_purchased == 2):
    print('You have earned 5 points')
# if books_purchased == 4 then 15 points are awarded
elif(books_purchased == 4):
    print('You have earned 15 points')
# if books_purchased == 6 then 30 points are awarded
elif(books_purchased == 6):
    print('You have earned 30 points')
# if books_purchased >= 8 then 60 points are awarded
elif(books_purchased >= 8):
    print('You have earned 60 points')