# import random
#
# for t in range(1,10):
#     print(random.randint(1,1000))

count = 0
def sum_recursion(k):
    global count
    if(k >0):
        count+= 1
        result = k + sum_recursion(k-1)
    else:
        result = 0
    return result

print(sum_recursion(4))
print(f'number of calls {count}')

print(655%15)