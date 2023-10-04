# This program displays a stair_step pattern
NUM_STEPS = 6

for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='') #here we have a space for every line iteration a new space is added for each new row
    print('#')


#EXPLANATION BELOW
# In line 1, the expression range(NUM_STEPS) produces an iterable containing the following
# sequence of integers:
# 0, 1, 2, 3, 4, 5
# As a result, the outer loop iterates 6 times. As the outer loop iterates, variable r is assigned
# the values 0 through 5. The inner loop executes as follows:
# • During the outer loop’s first iteration, the variable r is assigned 0. A loop that is written
# as for c in range(0): iterates zero times, so the inner loop does not execute at
# this time.
# • During the outer loop’s second iteration, the variable r is assigned 1. A loop that is
# written as for c in range(1): iterates one time, so the inner loop iterates once,
# printing one space.
# • During the outer loop’s third iteration, the variable r is assigned 2. A loop that is written
# as for c in range(2): will iterate two times, so the inner loop iterates twice,
# printing two spaces, and so forth.