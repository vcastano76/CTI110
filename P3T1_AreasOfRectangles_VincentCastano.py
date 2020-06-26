# Vincent Castano
# P3T1_AreasOfRectangles_CastanoVincent
# Created on June 26, 2020
# This program will prompt the user to input the dimensions of these rectangles to determine which area is greater or the same.

# Get the dimensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Determine ther area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.

if area1 > area2:
    print('Rectangle 1 has the greatest area.')
elif area2 > area1:
    print('Rectangle 2 has the greatest area.')
else:
    print('Both rectangles have the same area.')
