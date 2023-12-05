#this program gets three names from the user
# and writes them to a file

def main():
    #Get three names
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    #open a file named friends.txt
    #to clear confusion...we have a text file name 'friends.txt'
    #we are creating a file in memory named myfile that we use to open, write the names
    #of our friends name that we are inputing from the user
    myfile = open('friends.txt', 'w')

    #write the names to the file
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    #Close the file
    myfile.close()

#call the main function
if __name__ == '__main__':
    main()