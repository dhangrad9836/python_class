#take a list of values and add up
def summ(L):
    #declare and initialize any values that you intend to return
    addVals = 0

    for x in L:
        addVals = addVals + x
    return addVals

L = [1,2,3,4,5,8]

addL = summ(L)

print(addL)