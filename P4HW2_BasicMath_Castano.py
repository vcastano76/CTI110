# CTI-110
# P4HW2-BasicMath
# Vincent Castano
# Created on July 2, 2020.
# This program prompts the user to enter a number from the menu 1-4.
# Then, the user is prompted to enter two numbers and the result is provided.
# If the user enters a number beyond 4, then an error occurs.

print("1. Add Numbers");
print("2. Subtract Numbers");
print("3. Multiply Numbers");
print("4. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    elif choice == 4:
        exit();
else:
    print("Wrong input. Display a number from the menu!");
