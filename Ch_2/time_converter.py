#Get a number of seconds from the user.
total_seconds = float(input('Enter a number of seconds: '))

# Get the number of hous
#note that there are 3600 seconds in one hour and use interger division // so we don't have any fraction parts
hours = total_seconds // 3600

#Get the number of remaining minutes.
#first calculate the total number of minutes
#Next calculate with % operator to get the number of remaining minutes
minutes = (total_seconds // 60) % 60

#Get the number of remaining sedonds
seconds = total_seconds % 60

#Display the results
print('Here is the time in hours, minutes, and seconds: ')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)