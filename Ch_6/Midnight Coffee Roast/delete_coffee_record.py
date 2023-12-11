#this program allows the user to delete
#a record in the coffee.txt file.

# Needed for the remove and rename functions
import os

def main():
    #Create a bool value to use as a flag
    found = False

    #Get the coffee to delete.
    search = input('Which coffee do you want to delete? ')

    #open the original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #Create and open a new temp file
    temp_file = open('temp.txt', 'w')

    ############################################################

    #Read the first record's description field.
    descr = coffee_file.readline()

    #Read the rest of the file ...in a whild loop
    while descr != '':
        qty = float(coffee_file.readline())

        #Strip the \n from the description
        descr = descr.rstrip('\n')

        #if this is not the record to delete, then
        #write it to the temporary file.
        if descr != search:
            #write the original record variable to the temp file
            # if it's not found as the search value
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
        else:
            #Set the found flag to True.
            # the search value will end here and will not be copied to the temp_file
            found = True

        #Read the next description
        descr = coffee_file.readline()

    #Close the coffee and temporary file
    coffee_file.close()
    temp_file.close()

    #Delete the original coffee.txt file
    os.remove('coffee.txt')

    #Rename the temp file to the orignal name of coffee.txt
    os.rename('temp.txt', 'coffee.txt')

    #if the search value was not found in the file
    #Display a message.
    if found:
        print('The file has been updated.')
    else:
        print('The item was not found in the file. ')

#Call the main function
if __name__ == '__main__':
    main()