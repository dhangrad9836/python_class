# print(f"{20%4}")

# recursive call
def GCD(a, b):
    # write base case
    if b == 0:
        return a

    else:
        # recursive case: gcd(a, b)=gcd(b, a%b) assumption a<b
        r = a % b
        gcdab = GCD(b, r)

        return gcdab


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    gcd_ab = GCD(a, b)

    print(f"GCD of {a}, {b} is {gcd_ab}")


main()
