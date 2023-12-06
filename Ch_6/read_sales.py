#this program reads all of the values in
#the sales.txt file

def main():
    #open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    #Read the first line from the file, but
    #don't convert to a number yet. We still
    # need to test for an empty string
    line = sales_file.readline()

    #As long as an empty string is not returned
    #From readline, continue processing
    while line != '':
        #convert contents in line to a float
        amount = float(line)

        #Format and display the amount.
        print(f'{amount:.2f}')

        #remember this is inside a while loop so we are reading
        # at the end of of the file
        #read the next line.
        line = sales_file.readline()

    #Close the file
    sales_file.close()

#Call the main function
if __name__ == '__main__':
    main()

