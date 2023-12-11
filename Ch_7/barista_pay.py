#this program calculates the gross pay for
#each of megans employees

#NUM_EMPLOYEES is used as a constant for the size of the list
NUM_EMPLOYEES = 6

def main():
    #Create a list to hold employee hours.
    hours = [0] * NUM_EMPLOYEES

    #Get each employee's hours worked.
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Hours worked by employee {index + 1}: '))

    #get the hourly pay rate.
    pay_rate = float(input('Hourly pay rate: '))

    #Display each employees gross pay.
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'Gross pay for employee {index + 1}: '
              f'${gross_pay:,.2f}')

#Call the main function
if __name__ == '__main__':
    main()