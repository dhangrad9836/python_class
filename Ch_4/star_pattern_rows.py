# for row in range(8):
#     for col in range(6):
#         print('*', end='')
#     print()

# This program displays a rectangular pattern
# of asteriks.
rows = int(input('How many rows? '))
cols = int(input('How many columns? '))

for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()