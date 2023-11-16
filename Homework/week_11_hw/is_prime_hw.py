# question 1...
#is_prime function that check whether a number is prime or not
def is_prime(num):
    for i in range(2, num):
        if(num % i) == 1:
            return "Prime number"
            break
        else:
            return "not prime"
            break


def main():
    #initialize number_prime to zero
    number_prime=0
    #take in user input
    prime_number_checker = input("Enter a number to check if it's prime: ")
    while prime_number_checker != '0':
        #validate that user enters a number
        for i in prime_number_checker:
            if ord(i) not in range(48,58):
                print("Not a number:")
                #prime_number_checker = input("Enter a valid number: ")
            else:
                #call the is_prime function and pass in the users number
                number_prime= is_prime(int(prime_number_checker))
        #print the users results
        print(number_prime)
        #loop re-runs here to ask the user to enter a number or 0 to quit
        prime_number_checker = input("Enter another number or enter 0 to quit: ")

main()