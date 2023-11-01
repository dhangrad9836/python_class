# This function takes a list of values and adds them up
def summ(L, start, end):
    # first check if only 2 numbers in list
    if end - start == 1:
        return L[start] +L[end]

    else:
        #divide the list here
        # start = 0, end = 7
        start1 = start
        end1 = (start+end)//2

        #second half of list
        start2 = end1 + 1
        end2 = end

        return summ(L, start1, end1) +summ(L, start2, end2)

    # main function
def main():
    L=[1, 2, 3, 4, 5, 6, 7, 8]

    start = 0
    #last number of list
    end = len(L) - 1

    addL = summ(L, start, end)
    print(addL)

# Call main
main()