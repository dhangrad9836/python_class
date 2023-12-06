#this program uses the for loop to read
#All of the values in the sales.txt file

def main():
    #Open the sales.txt file for reading
    sales_file = open('sales.txt', 'r')

    #Read all the lines from the file using for loop without any testing
    #ie for end of line or empty spaces
    for line in sales_file:
        #convert line to a float.
        amount = float(line)
        #format and display the amount.
        print(f'{amount:.2f}')

    #close the file.....make sure this is done outside the loop
    sales_file.close()

#call the main function
if __name__ == '__main__':
    main()