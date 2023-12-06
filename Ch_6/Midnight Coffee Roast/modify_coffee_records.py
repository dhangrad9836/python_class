#this program allows the user to modify the quantity
#in a record in the coffee.txt file

#import os library here for the remove and rename functions
import os

def main():
    #create a bool value and rename functions
    found = False

    #Get the search value and the new quantity.
    search = input('Enter a description to searchfor: ')
    new_qty = int(input('Enter the new quantity: '))

    # 1. open the original file FIRST THING TO DO
    coffee_file = open('coffee.txt', 'r')

    # 2. Create and open the temporary file 'temp.txt' this file will be used to write all the contents
    # from the original file and copied to the this file
    temp_file = open('temp.txt', 'w')

    # 3. Read the first record's description field.
    descr = coffee_file.readline()

    # 4. Read the rest of the file
    while descr != '':
        #Read the qty field...FIRST convert to float
        qty = float(coffee_file.readline())

        #strip the \n from the description.
        descr = descr.rstrip('\n')

        # 5....NOW NEW Material
        # Write either this record to the temporary file.
        # or the new record if this is the one to be modified
        if descr == search:
            #Write the new modified record to the temp file.
            #Remember it has to be wriiten in the same order and we will use the
            #same descr variable but the new information is new_qty which will replace the old qty information
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')

            #Set the flag to true
            found = True

        else:
            # Write the original record to the temp file by using
            # the original variables of descr and qty...we will not use new_qty here as the
            # search results did not find a record so we will just add the new record here
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

        #Read the next description or while loop ends here
        descr = coffee_file.readline()

    #Close the coffee file and temp file temp_file file outside the if/else statements
    coffee_file.close()
    temp_file.close()

    #DELETE THE ORIGINAL coffee.txt file
    os.remove('coffee.txt')

    #Rename the NEW TEMP FILE to the original name so temp.txt becomes coffee.txt
    os.rename('temp.txt', 'coffee.txt')

    #If the search value was not found in the file
    #display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

#Call the main function
if __name__ == '__main__':
    main()