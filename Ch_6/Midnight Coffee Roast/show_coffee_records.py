#This program displays the records in the
#coffee.txt file

def main():
    #Open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #read the first record's description field
    descr = coffee_file.readline()

    #Read the rest of the file
    while descr != '':
        #Read the qty field
        qty = float(coffee_file.readline())

        #Strip the \n from the description
        descr = descr.rstrip('\n')

        #Display the record
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')

        #while loop and read tne next line or end the while loop
        descr = coffee_file.readline()

    #Close the file
    coffee_file.close()

#Call the main function
if __name__ == '__main__':
    main()