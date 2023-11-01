def sum_recursion(k):
    if(k > 0):
        result =  k + sum_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\n Sum of 1 to n numbers: ")
print(sum_recursion(6))