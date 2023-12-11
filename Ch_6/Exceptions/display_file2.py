#this program displays the contents of a file or throws an exception

def main():
    #Get the name of a file
    filename = input('Enter a filename: ')

    try:
        #open the file.
        infile = open(filename, 'r')

        #Read the file's contents
        contents = infile.read()

        #display the files contents
        print(contents)

        #close the file
        infile.close()
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

#Call the main function
if __name__ == '__main__':
    main()