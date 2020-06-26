# CTI-110
# P3HW2 - BasicMath
# Vincent Castano
# This program asks the user to enter two numbers, display a menu, and then
# prompt the user to enter their choice of mathematical operation.

# I'm calling the variable defining the input statements
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

# Here, I am assuming that no decimals are going to occur so I'm entering integers into the string.

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

# I am using If/Else If statements regarding my order of operations and how I want them displayed in the calculator.
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

# The user will be prompted to enter a valid operation.
    else:
        print('You have not typed a valid operator, please run the program again.')

# Add again() function to calculate() function
    again()

# I'm calling another variable to prompt the user whether they wish to continue.
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
