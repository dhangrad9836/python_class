# 2. A vineyard owner is planting several new rows of grapevines, and needs to know how many
# grapevines to plant in each row. She has determined that after measuring the length of a
# future row, she can use the following formula to calculate the number of vines that will fit
# in the row, along with the trellis end-post assemblies that will need to be constructed at
# each end of the row:

# Get user input for: row, endpost, and vine space
# Convert all inputs to floats

# Ask the user to input the length of the row in feet and convert input string to float
ROW_LENGTH = float(input('Enter the length of the row in feet: '))

# Ask the user to input the end-post assembly in feet and convert input string to float
END_POST = float(input('Enter the endpost assembly in feet: '))

# Ask the user to input the amount of space between the vines in feet and convert input string to float
SPACE_BETWEEN_VINES = float(input('Enter the space between the vines in feet: '))

# Formula: V = (R - 2E)/S
# Our version of formula:  V = (ROW_LENGTH - (2 * END_POST))/SPACE_BETWEEN_VINES
# V is the number of grapevines that will fit in the row.
# ROW_LENGTH is the length of the row, in feet.
# END_POST is the amount of space, in feet, used by an end-post assembly.
# SPACE_BETWEEN_VINES is the space between vines, in feet.

# Calculate the number of vines that will fit in the row using the given fomula.
V = (ROW_LENGTH - (2 * END_POST)) / SPACE_BETWEEN_VINES

# Display the number of grapevines that will fit in the row
print(f'The number of grapevines that will fit in the row: {V:.1f} grapevines')