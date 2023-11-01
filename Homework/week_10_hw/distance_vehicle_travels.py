# formula distance = speed x time
# total hours end at what user enters
# will need a range to start and stop (stop will be the total hours entered by user)
# inside loop enter formula and speed vehicle is traveling
# every iteration and hour increases the speed multiply by that number
# print every iteration hour and distance traveled

# Have user enter the speed of the vehicle
vehicle_speed = int(input('What is the speed of the vehicle in mph? '))
# validate the user enters a number greater than zero
while vehicle_speed <= 0:
    print('Vehicle speed should be greater than zero.')
    vehicle_speed = int(input('Please re-enter the speed of the vehicle in mph? '))


# Have user enter how many hours it traveled
total_hours_traveled = int(input('How many hours has it traveled? '))
# validate the user enters a number greater than zero
while total_hours_traveled <= 0:
    print('Total hours should be greater than zero.')
    total_hours_traveled = int(input('Please re-enter the total number of hours traveled? '))

# initialize a distance variable to calculate the distance for each hour traveled
distance = 0

# print heading for the distance for each hour traveled
print(f'Hour\t\t Distance Traveled')
print('______________________________')

for hour in range(1, total_hours_traveled + 1):

    # calculate the distance for each hour traveled
    # formula: distance = time * speed
    distance = hour * vehicle_speed

    # Print the output for each hour the distance traveled
    print(f'{hour}\t\t\t\t\t{distance}')


