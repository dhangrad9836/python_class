#This program uses the writelines method to save
#a list of strings to a file

def main():
    #Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    #Opena file for writing
    outfile = open('cities2.txt', 'w')

    #write the list to the file with a for loop
    for item in cities:
        outfile.write(item + '\n')

    #Close the file
    outfile.close()

#Call the main function
if __name__ == '__main__':
    main()