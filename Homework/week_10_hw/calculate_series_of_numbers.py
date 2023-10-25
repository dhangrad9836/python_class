# Calculate 1/30 + 2/29....+ 30/1
# So it's a fraction where the numerator is increasing and the denominator decreases
# probably use a range function with also having an incrementing number increasing inside
# the same loop and then you can use the number that is increasing as the numerator
# and the range as it's decreasing as the denominator

# Define an variable for the numerator outside of the loop
# that will increase inside everytime the loop runs
numerator = 0

# define a variable named total to keep the sum of the calculation
# inside everytime the loop iterates
total = 0

# define a for loop with range of numbers that decreases from 30 to 1
for denominator in range(30, 0, -1):
    # this number will be used to calculate for the increasing numerator
    numerator += 1

    # perform the calculation
    total += (numerator / denominator)
    #print(total)

# print the running total of the calculation
print(f'The total is: {total:.2f}')




