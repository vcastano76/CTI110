# CTI-110
# P3HW1 - Color Mixer
# Vincent Castano
# Created on June 26, 2020
# This program is looking at two primary colors and the secondary colors they produce.
# If the user tried to enter anything beyond red, yellow, and blue, then an error will occur.

# I'm identifying my primary colors and prompting for user input.
primary_colors = ('red', 'yellow', 'blue')
user_input = ''

# I'm declaring my variables and order of operation for the first combination.
def get_color(ordinal):
    color = input(f'{ordinal} primary color: \t').lower()
    if color in primary_colors:
        return color
    else:
        print('Invalid entry, please enter red, yellow, or blue')
        return get_color(ordinal)

#I'm declaring my variables and order of operation for the second combination.
def mix_colors(color1, color2):
    print('\nMixing colors...')
    if color1 == color2:
        return color1.capitalize()
    elif (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        return 'Purple'
    elif (color1 == 'yellow' and color2 == 'blue') or (color1 == 'blue' and color2 == 'yellow'):
        return 'Green'
    else:
        return 'Orange'

# I'm defining how to display the results.
def display_results(color1, color2, mixed_color):
    print(f'{color1.capitalize()} and {color2.capitalize()} = \t{mixed_color}\n')

# At this point, I'm giving the user the opportunity to quit if they enter an invalid color.
def keep_going():
    global user_input
    try: 
        user_input = input("Enter 'q' to quit or press any other key to continue mixing colors: \t")[0:1].lower()
    except:
        print('Invalid entry!')
        keep_going()

# I'm defining how I want the prompts to appear and adding a goodbye statement if the user wants to quit the program.
while user_input != 'q':
    print('\nPlease enter two primary colors (red, yellow, blue).')
    color1 = get_color('First')
    color2 = get_color('Second')
    result = mix_colors(color1, color2)
    display_results(color1, color2, result)
    keep_going()
else:
    print('Goodbye!')
