# sorted list
sorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def bin_search(lst, val, low, high):
    if(low > high):
        return None
    else:
        mid = (low + high) // 2
        if(val > lst[mid]):
            return bin_search(lst, val, mid+1, high)
        elif (val < lst[mid]):
            return bin_search(lst, val, low, mid-1)
        else:
            return mid

i = bin_search(sorted, 6, 0, len(sorted) - 1)

print("index of 6: ", i)