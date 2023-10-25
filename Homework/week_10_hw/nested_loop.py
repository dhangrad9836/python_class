NUM_OF_STEPS = 6

# print a star in first column for each row iteration
# also in the last row each column has a star

for r in range(NUM_OF_STEPS):
    for c in range(r):
        if(c == r):
            print('', end='')
    print(' #')
