# CTI-110
# P3LAB - Debugging
# Vincent Castano
# Created on June 26, 2020
# Rewriting the code and using the proper conventions and alignment and indentation.

# Without constants to represent the grade thresholds, the program will not execute properly.
# So, I am making up some constants

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Next we need a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade
if score >= A_SCORE:
    print ('Your grade is A.')
else:
    if score >= B_SCORE:
        print ('Your grade is B.')
    else:
        if score >= C_SCORE:
            print ('Your grade is C.')
        else:
            if score >= D_SCORE:
                print ('Your grade is D.')
            else:
                print ('Your grade is F.')
