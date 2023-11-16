import random
# question 5...
#random_gen function to generate a single random number between -25 through 25
def random_gen():
    # Get a random number
    return random.randint(-25, 25)

#add function that takes in two parameters
#it keeps adding up values until it equals zero
def add(total, random_number):
    #running total of random number and the total
    add_total = total + random_number
    return add_total



#global variable subsetsum
subsetsum = 0
#main function
def main():
    # global variable subsetsum declared inside main function
    global subsetsum
    #count variable to keep count of how many times values are generated
    count = 0
    while True:
        #store the random number inside int_num variable
        int_num = random_gen()
        #call the add function with the subsetsum overall total and the random number
        # and store the value inside added_value
        added_value = add(subsetsum, int_num)
        #new total of subsetsum is updated
        subsetsum = added_value
        #print(subsetsum)
        if subsetsum == 0:
            print('Subset sum is zero')
            break
        else:
            #add one to the count if total is not zero
            count += 1
            #call the random_gen function to re-run the loop
            random_gen()
    print(f'Total count is {count}')

main()