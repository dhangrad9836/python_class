#This program displays the total of the
#amounts in the sales_data.txt file

def main():
    #Intialize an accumulator.
    total = 0.0

    try:
        #Open the sales_data.txt file
        infile = open('sales_data.txt','r')

        #Read the values from the file and
        #accumulate them
        for line in infile:
            amount = float(line)
            total += amount
        print(f'{total}')

        #Close the file
        infile.close()

    #Multiple exceptions
        #this exception is if the file does not exist
    except IOError:
        print('An error occurred trying to read the file')
        #this exception is if non-numberic data is in the file
    except ValueError:
        print('Non-nummeric data found in the file.')

    except:
        print('An error occurred.')

#Call the main function
if __name__ == '__main__':
    main()