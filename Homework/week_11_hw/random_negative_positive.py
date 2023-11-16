import random
# question 5..
# global variable subsetsum
#subsetsum = 0
# add function that adds user inputs
def random_gen():
    # Get a random number
    return random.randint(-25, 25)


def add(total, random_number):

    add_total = total + random_number
    return add_total




subsetsum = 0
def main():
    global subsetsum

    count = 0
    while True:
        int_num = random_gen()
        added_value = add(subsetsum, int_num)
        subsetsum = added_value
        #print(subsetsum)
        if subsetsum == 0:
            print('Total is zero')
            break
        else:
            count += 1
            random_gen()
    print(f'Total count is {count}')

main()