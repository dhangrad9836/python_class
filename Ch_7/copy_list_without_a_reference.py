# Create a list with values.
list1 = [1, 2, 3, 4]
# Create an empty list.
list2 = []
# Copy the elements of list1 to list2.
#this creates an exact copy of the list but not referencing the list
for item in list1:
    list2.append(item)

#a simpler way is to concatenate the list
# Create a list with values.
list1 = [1, 2, 3, 4]
# Create a copy of list1.
list2 = [] + list1