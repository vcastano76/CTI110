# I'm writing a program with pseudocode that creates a turtle graphic
# June 20, 2020
# CTI-110 P2HW2-Turtle Graphic
# Vincent Castano

# First I need to load the turtle module into the memory so Python can read it.
import turtle

# I'm telling the turtle where I want the line drawn (x, y), I want the line drawn up
turtle.goto (0, 180)
# I'm formatting the proper display at this point.
turtle.write ('North')
# I'm telling the turtle to go back to the center (x, y).
turtle.goto (0, 0)
# I'm telling the turtle where I want the line drawn (x, y). I want the line drawn down.
turtle.goto (0, -180)
# I'm formatting the proper display at this point.
turtle.write ('South')
# I'm sending the turtle back to the center (x, y).
turtle.goto (0, 0)
# I'm sending the turtle to draw a line to the right (x, y).
turtle.goto (180, 0)
# I'm formatting the proper display at this point.
turtle.write ('East')
# I'm sending the turtle back to the center.
turtle.goto (0, 0)
# I'm sending the turtle to draw a line to the left (x, y)
turtle.goto (-180, 0)
# I'm formatting the proper display at this point.
turtle.write ('West')
# I'm sending the turtle back to the center.
turtle.goto (0, 0)
# I'm sending the turtle to another starting point for my circle (x, y).
turtle.goto (0, -45)
# I'm telling the turtle to draw a circle with a radius of 45 degrees.
turtle.circle (45)




