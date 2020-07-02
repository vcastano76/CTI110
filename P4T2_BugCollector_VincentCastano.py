# The program asks the user for the amount of bugs collected each day for 5 days and then displays a total.
# Created on July 2, 2020
# CTI-110 P4T2 - Bug Collector
# Vincent Castano

total_bugs = 0

#The loop asks the user for the amount of bugs collected each day.
for day in range(5) :
	bugs = int(input("How many bugs did you collect today?"))
	total_bugs += bugs
	
#Displays the amount of bugs collected.
print("\nYou have collected", format(total_bugs, ",.0f"), "bugs.")
