#this program reads the contents of the pholosophers.txt
#file one line at at time

def main():
    #open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    #read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #close the file
    infile.close()

    #print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

#Call the main function
if __name__ == '__main__':
    main()