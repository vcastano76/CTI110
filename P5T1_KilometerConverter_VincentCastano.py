# This program asks the user to enter a distance in kilometer
# Then coverts that distance to miles.
# Created on July 7, 2020
# CTI-110 P5T1_KilometerConverter
# Vincent Castano

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
