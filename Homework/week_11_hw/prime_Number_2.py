def is_prime(num):
    for i in range(2, num):
        if(num % i) == 1:
            return "Prime number"
            break
        else:
            return "not prime"
            break


def main():

    prime_number_checker = input("Enter a number to check if it's prime: ")
    while prime_number_checker != 0:
        for i in prime_number_checker:
            if ord(i) not in range(48,58):
                print("Not a number:")
                prime_number_checker = input("Enter a valid number: ")
            else:
                pass
        print(is_prime(int(prime_number_checker)))
        prime_number_checker = input("Enter another number or enter 0 to quit: ")

main()

