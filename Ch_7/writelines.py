#This program uses the writelines method to save
#a list of strings to a file

def main():
    #Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    #Opena file for writing
    outfile = open('cities.txt', 'w')

    #Write the list to the file
    outfile.writelines(cities)

    #close the file
    outfile.close()

#Call the main function
if __name__ == '__main__':
    main()