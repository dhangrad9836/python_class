#This program divides a number by another number

def main():
    #Get two numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    #Divide num1 by num2 and display the result
    #If num2 is not 0, divide num1 by num2
    #and display the result.
    if num2 != 0:
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')
    else:
        print('Cannot divide by zero.')

#call the main function
if __name__ == '__main__':
    main()