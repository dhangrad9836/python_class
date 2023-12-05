#numbers = [5, 10, 15, 20]
#range returns an iterable object of values not a list
#this converts the range object to a list
#basically the iterable object is passed to the list() function and returns a list
numbers = list(range(5))
#print(numbers)

# will make 5 copies of 0 and join them in a list... [0, 0, 0, 0, 0]
num_list = [0] * 5
#print(num_list)

list_nums = [1,2,3,4]
for num in list_nums:
    num = 99
#print(list_nums)

my_list = [10,20,30,40]
index = 0
while index < 4:
    #print(my_list[index])
    index += 1

#so here the for loop will assign index values 0,1,2,3, thus printing only those values
names = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
for index in range(len(names)):
    print(names[index])