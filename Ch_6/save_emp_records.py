#This program gets employee data from the user and
#saves it as records in the employee.txt file.

def main():
    #Get the number of employee records to create.
    num_emps = int(input('How many employee records ' +
                         'do you want to create? '))

    #Open a file for writing.
    emp_file = open('employees.txt', 'w')

    #Get each employee's data and write it to the file.
    #remember that the plus 1 is for displaying purposes so it will not display as 0 and as 1
    for count in range(1, num_emps + 1):
        #get the data for an employee.
        print(f'Enter data for employee #{count}')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        #Write the data as a record to the fild.
        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')

        #Display a blank line
        print()

    #close the file....remember to do this outside of the loop
    emp_file.close()
    print('Employee records written to employees.txt.')

#Call the main function
if __name__ == '__main__':
    main()