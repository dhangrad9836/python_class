#This program demonstrates how numbers
#must be converted to a text file

def main():
    #open a file for writing
    outfile = open('numbers.txt', 'w')

    #Get three numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    #write the numbers to the file. and convert to a string
    #as numbers must be converted to a string before written
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    #close the file
    outfile.close()
    print('Data written to numbers.txt')

#call the main fuction
if __name__ == '__main__':
    main()