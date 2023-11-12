import math

# 4. Write a program that asks the user to enter the radius of a circle. The program should cal-
# culate and display the area and circumference of the circle using πr^2 for the area and 2πr
# for the circumference.
# Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
# to the start of the program and then use "math.pi" wherever you need the value of pi in
# the program.

# Ask the user for input the radius of a circle
radius_of_circle = float(input('Enter the radius of a circle to find the area and circumference: '))

# value of PI
PI = math.pi

# calculate the area of a circle using πr^2 for the area
area_of_circle = PI * (radius_of_circle ** 2)

# calculate the circumference of a circle using 2πr for the circumference
circumference_of_circle = 2 * PI * radius_of_circle

# display the area and circumference of the circle
print(f'The area of the circle is: {area_of_circle:.2f} \n'
      f'The circumference of the circle is: {circumference_of_circle:.2f}')