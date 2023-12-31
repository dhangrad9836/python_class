#file one line at at time

def main():
    #open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    #read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #Strip the \n from each string
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    #close the file
    infile.close()

    #print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

#Call the main function
if __name__ == '__main__':
    main()