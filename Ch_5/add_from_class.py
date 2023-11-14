def summ(L, start, end):
# first check if only two elements are only in the list, if yes then just
# add the two elements up only,you will check of the elements of the list is only index of 1
#basically if it equals to 1 which means that you only have two elements in a list [0,1]
# L[start] = 0 and L[end] = 1 so 1-0 = 1 ..these are the indexes of only two elemnents in a list
# so you only need to add up those two elements. and it would return those two elements added up
    #you need this bottom condition to break the recursive call or it will not stop
    #to say that you have only two elements left to check
    if end-start == 1:
        return L[start] + L[end]

    else:
        #contine with the list to add up...
        #divide the list here
        # start = 0 and end = 7
        start1 = start
        end1 = (start + end)//2

        #second half of the list
        start2 = end1 + 1
        end2 = end

        return summ(L, start1, end1) + summ(L, start2, end2)



#main prgram
def main():
    L = [1,2,3,4,5,6,7,8]
    #initialize the start with index of 0 and end with index of 7
    start = 0
    end = len(L)-1
    #pass the arguments to the summ() function...the list, start and end
    addL = summ(L, start, end)

    print(addL)

main()