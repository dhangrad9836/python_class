# This program demonstrates what happens when you
# Change the value of a parameter

# Define main function
def main():
    value = 99
    print(f'The value is {value}')
    change_me(value)
    print(f'Back in main function the value is {value}')

def change_me(arg):
    print('I am changing the value')
    arg = 0
    print(f'Now the value is {arg}')

# call main function
main()
