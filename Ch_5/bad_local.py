# Definition of the main function
def main():
    get_name()
    print(f'Hello {name}.')     # This causes an error outside of scope

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')

# Call the main function
main()