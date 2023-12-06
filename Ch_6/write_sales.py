#this program prompts the user for sales amounts
#and writes those amounts to the sales.txt file

def main():
    #Get the number of days.
    num_days = int(input('For how many days do ' +
                         'you have sales: '))

    #open a new file name sales.txt
    sales_file = open('sales.txt', 'w')

    #get the amount of sales for each day and write
    #it to the file
    for count in range(1, num_days + 1):
        #get the sales for a day.
        sales = float(input(
            f'Enter the sales for day #{count}: '))

        #write the sales amount to the file.
        sales_file.write(f'{sales}\n')

    #close the file. ******important*****
    #make sure this is outside of the loop
    sales_file.close()
    print('Data written to sales.txt')

#call the main function
if __name__ == '__main__':
    main()