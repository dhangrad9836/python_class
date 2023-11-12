#A prime number is a number that can only be divided by itself and 1 without remainders.
#take a number as input from user
# validate that it's a number and nothing else
# if not a number prompt to re-enter input
# validate in is_prime(N) function that N as argument and outputs if N is prime or not
# return to main function


def main():
    # have user enter a number and check whether it's a prime number
    checkIfPrimeNumber = input("Enter a number to check if it's a prime number or 0 to quit: ")

    # while loop to validate if user's input is a number
    while checkIfPrimeNumber != '0':
        for N in checkIfPrimeNumber:
            if ord(N) not in range(48, 58):
                print("Not a valid input\n")
                checkIfPrimeNumber = input("Enter a number to check if it's a prime number or 0 to quit: ")
            else:
                # call is_Prime function with N as argument
                pass
        valid_num = int(N)
        #print("Enter 0 to quit")
    is_Prime(valid_num)

# call main function
main()

# is_Prime function that check the user input if it's prime number
def is_Prime(num):
    print(num)