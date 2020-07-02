# This program uses nested loops to draw the pattern.
# Created on July 2, 2020.
# CTI-110 P4HW3-Nested Loops
# Vincent Castano

steps=6
for r in range(steps):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
