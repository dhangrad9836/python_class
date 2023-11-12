def add_args(args):
    sum_args = 0

    for x in args:
        sum_args += x

    return sum_args


def main():
    # prompt user
    x = input("Enter number or 0 to quit:  ")

    # empty list to store numbers
    list_of_args = list()

    # for c in x:
    #     if ord(c) not in range(48, 58):
    #         print("not a number")
    #         return
    #     else:
    #         pass

    while x != '0':

        for c in x:
            if ord(c) not in range(48, 58):
                print("not a number")
                return
            else:
                pass

        list_of_args.append(int(x))
        x = input("Enter number or 0 to quit:  ")

    print("Sum of args", add_args(list_of_args))
    return


main()
