#this program demonstrates how numbers that
#are read from a file must be converted from strings to a numerical value
#Before they are used in a math operation

def main():
    #open a file for reading using the 'r'
    infile = open('numbers.txt','r')

    #Read three numbers from the file and conver
    # back to int or whatever numerical value so their will not be any mathematical problems
    num1 = int(infile.readline())
    num2= int(infile.readline())
    num3 = int(infile.readline())

    #close the file

    #add the numbers
    total = num1 + num2 + num3

    #display the numbers
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')

#Call the main function
if __name__ == '__main__':
    main()