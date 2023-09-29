# A cookie recipe calls for the following ingredients:
# • 1.5 cups of sugar
# • 1 cup of butter
# • 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program that
# asks the user how many cookies he or she wants to make, then displays the number of cups
# of each ingredient needed for the specified number of cookies.

# find how much does each ingredient take for one cookie?
# ask user to input how many cookies they want to make
# after input convert input string to float
# do conversion for each individual ingredient
# print to screen in formatted output


# ask user to input how many cookies they want to make
total_cookies_to_make = float(input('Enter how many cookies do you want to make: '))

# enter constants for each ingredient
# Base number of cookies used for ingredient conversion
BASE_NUMBER_OF_COOKIES = 48
# amount of SUGAR for one cookie
SUGAR_INGREDIENT = 1.5/BASE_NUMBER_OF_COOKIES
# amount of BUTTER for one cookie
BUTTER_INGREDIENT = 1/BASE_NUMBER_OF_COOKIES
# amount of FLOUR for one cookie
FLOUR_INGREDIENT = 2.75/BASE_NUMBER_OF_COOKIES

# do ingredient conversions
total_sugar = total_cookies_to_make * SUGAR_INGREDIENT
total_butter = total_cookies_to_make * BUTTER_INGREDIENT
total_flour = total_cookies_to_make * FLOUR_INGREDIENT
# display results
# print(f'The amount of sugar for {total_cookies_to_make:.0f} cookies is {total_sugar:.1f} cups.\n' +
#       f'The amount of butter for {total_cookies_to_make:.0f} cookies is {total_butter:.1f} cups.\n' +
#       f'The amount of flour for {total_cookies_to_make:.0f} cookies is {total_flour:.1f} cups.')

print(f'The ingredients to make {total_cookies_to_make:.0f} cookies are as follow:\n*\t {total_sugar:.1f} cups of sugar \n'
      f'*\t {total_butter:.2f} cups of butter\n*\t {total_flour:.2f} cups of flour')