# This program demonstrates passing two string
# arguments to a function

# Define main function
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reversed_name(first_name, last_name)

def reversed_name(first, last):
    print(last, first)

# call main function
main()