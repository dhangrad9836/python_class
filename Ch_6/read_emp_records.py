#This program displays the records that are
#in the employees.txt file

def main():
    #Open the employees.txt file
    emp_file = open('employees.txt', 'r')

    #Read the first line from the file, which is
    #the name field of the first record.
    name = emp_file.readline()

    #If a field was read, continue processing ...use a while loop
    while name != '':
        #Read the ID number field...note that it keeps reading in a continuous order
        id_num = emp_file.readline()

        #Read the department field.
        dept = emp_file.readline()

        #strip the newlines from the fields.
        name = name.strip('\n')
        id_num = id_num.strip('\n')
        dept = dept.strip('\n')

        #Display the record.
        print(f'Name: {name}')
        print(f'ID: {id_num}')
        print(f'Dept: {dept}')
        print()

        #while loop either read the next record or while loop ends
        #only need to enter the first line to be read only
        name = emp_file.readline()

    #Close the file
    emp_file.close()

#Call the main function
if __name__ == '__main__':
    main()