#This program reads and displays the contents
#of the philosophers.txt file

def main():
    #Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    #Read the file's contents
    file_contents = infile.read()

    #Close the infile file that we opened to be stored into file_contents
    infile.close()

    #print the data that was read into memory
    print(file_contents)

#call the main function
if __name__ == '__main__':
    main()