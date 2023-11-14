#recursive function
def reverse(S, first, last):

    t1=S[first] #get the first character
    t2=S[last] #get the last character

    #Base cases
    if first==last:
        return t1 #or return t2

    if last==first+1:   #why plus 1 it would make the index 1 and not checking 0
        return t2+t1 #swap two characters..if they are equal then it will
                     # return both characters which will actually be the same character
                     #because if/when last==first it will be the same character they are indexed at
    #update the indexes
    first = first + 1
    last = last - 1

    #recursive call..aTb becomes b+reverse(T)+a
    rS = t2+reverse(S, first, last)+t1

    #the reversed string
    return rS


def main():
    T = input("Enter the target string ")

    print("Before reverse", T)

    #first call: target string = T, first index = 0, last index = len(T)-1
    rT = reverse(T, 0, len(T)-1)

    print("After reverse", rT)

#call main function
main()