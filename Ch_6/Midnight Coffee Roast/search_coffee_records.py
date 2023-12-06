#This program allows the user to search the
#coffee.txt file for records matching a description

def main():
    #Create a bool variable to use as a flag.
    found = False

    #Get the search value.
    search = input('Enter a description to search for: ')

    #Open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #Read the first record's description field.
    descr = coffee_file.readline()

    #Read the rest of the file...first while loop to make sure the file is not empty
    while descr != '':
        #Read the qty field and convert to float
        qty = float(coffee_file.readline())

        #Strip the \n from the description
        descr = descr.rstrip('\n')

        #Everything from this point above is everything that we know so far
        #Below we learn to search for values

        #Determine whether this record matches
        #The search value.
        if descr == search:
            #Display the record.
            print(f'Description: {descr}')
            print(f'Quantity: {qty}')
            print()
            #Set the flag to true
            found = True

            #Read the next line or end the while loop
        descr = coffee_file.readline()

    #Close the file
    coffee_file.close()

        #if the search value was not found in the file
        #Display a message
    if not found:
        print('That item was not found in the file.')

#Call the main function
if __name__ == '__main__':
    main()












