# CTI-110
# Vincent Castano
# Created on July 2, 2020
# p4t1a_castano
# The program creates 100 squares using nested loops

# I am calling the turtle
import turtle

# The next two codes tell where I want the squares drawn
turtle.right(180)

turtle.speed(0)

# The next series of codes indicate how many squares and along with length.
length = 505

for times in range (100):
  for endtimes in range (4):
    turtle.forward(length)
    turtle.right(90)
  length -= 5
