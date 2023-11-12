import random

def main():
    # have user enter how many number to generate
    userInput = input("Enter a number: ")
    while userInput != 0:
        if ord(userInput) not in range(48,58):
            print("Not a number\n")
            userInput = input("Enter a valid input: ")
        else:
            pass

    for count in range(userInput):
        # Get a random number
        number = random.randint(1, 100)

        # Display the number
        print(f'Number {count + 1} is {number}.')

# Call the main function
main()