#This program adds coffee inventory records to
#The coffee.txt file.

def main():
    #Create a variable to control the loop.
    another = 'y'

    #Open the coffee.txt file in append mode.
    #remember that append mode keeps the existing file and does not
    #Delete the contents inside the file
    coffee_file = open('coffee.txt',  'a')

    #Add records to the file.
    while another == 'y' or another == 'Y':
        #Get the coffee record data.
        print('Enter the following coffee data: ')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        #Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(f'{qty}\n') #remember to use function notation to bracket the variable qty
                                      #Because you cannot add concat the variable and the newline
        #Determine whether the user wants to add
        #another record to the file.
        print('Do you want to add another record? ')
        another = input('Y = yes, anything else = no: ')

    #Close the file....remember this needs to be outside of the loop
    coffee_file.close()

#Call the main function
if __name__ == '__main__':
    main()