input_range=10 #input from user
range_index=input_range #variable to count down
to_print="" #string that we want to print

#need to print from 10 +s till 1 +
for range_index in range(input_range, 0, -1):
    for val in range(range_index):
    	    #create printable string
            to_print="+" + to_print
    print(to_print)

    #reset the string to be printed
    to_print=""
