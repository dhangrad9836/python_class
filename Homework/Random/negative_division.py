# print(-8/2)
# print(-8//2)
# print(15 / 4)
# print(15 // 4)
# print(-15 // 4)

input_range = 10
range_index = input_range
to_print=""

for range_index in range(input_range, 0 -1):
    for val in range(range_index):
        to_print="+" + to_print
    print(to_print)

    to_print=""