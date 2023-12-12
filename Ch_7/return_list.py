#This program uses a function to create a list.
#The function returns a reference to the list.

def main():
    #Get a list with values stored in it.
    numbers = get_values()

    #Display the values in the list.
    print('The numbers in the list are: ')
    print(numbers)

#The get_values function gets a series of numbers
#From the user and stores them in a list. The
#Function returns a reference to the list.
def get_values():
    #Create an empty list
    values = []

    #Create a variable to control the loop
    again = 'y'

    #Get values from the user and add them to the  list
    while again == 'y':
        num = int(input('Enter a number: '))
        values.append(num)

        #Want to do this again?
        print('Do you want to add another number? ')
        again = input('y = yes, anything else = no: ')

    #Return the list of values
    return values

#Call the main function
if __name__ == '__main__':
    main()