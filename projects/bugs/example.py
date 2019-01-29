# we will need some turtles; one for each bug plus a spare
from turtle import Turtle

# This is just used to brighten up the colors of the bug paths a bit
lowlight = 50

# Here are the four bugs as turtle graphics Turtles
a = Turtle()
b = Turtle()
c = Turtle()
d = Turtle()

# This is a spare turtle used to draw connector lines
box = Turtle()

# Set the colors to be red, yellow, green and cyan. The 'lowlight' makes them a bit brighter
a.pencolor(255, lowlight, lowlight)
b.pencolor(255, 255, lowlight)
c.pencolor(lowlight, 255, lowlight)
d.pencolor(lowlight, 255, 255)

# s is the side of the table. I make it 390 for the cswonders graphics is 400 x 400 pixels
#   At the end of the program we determine how far each bug has traveled in pixels and divide
#   that by s to determine how far the bug went in units of s.
s = 390.

# s2 is half of s; used to set up our starting positions on the table
s2 = s/2

# Everybody lift up your pen
a.up()
b.up()
c.up()
d.up()

# Now go to your corners
a.setpos(-s2, s2)
b.setpos(s2, s2)
c.setpos(s2, -s2)
d.setpos(-s2, -s2)

# put your pends down
a.down()
b.down()
c.down()
d.down()

# make sure you are going to draw quickly
a.speed(1000)
b.speed(1000)
c.speed(1000)
d.speed(1000)
box.speed(1000)

# epsilon is the size of each bug step in pixels
epsilon = 1.0

# When the bugs are this close we consider them to be done
close_distance = 1.2

# This is how far bug 'a' has walked (in pixels)
a_cumulative = 0.

# Let's count how many steps we take so we can halt if something gets out of control
nCycles = 0

# We will use an infinite loop to allow the bugs to walk for as long as they need to
while True:
    
    # the turtle function .towards() gives us the angle from the turtle to another turtle
    a_to_b_angle = a.towards(b)
    b_to_c_angle = b.towards(c)
    c_to_d_angle = c.towards(d)
    d_to_a_angle = d.towards(a)
    
    # use .setheading() to set the turtle's heading; which we got the correct angles from the previous part
    a.setheading(a_to_b_angle)
    b.setheading(b_to_c_angle)
    c.setheading(c_to_d_angle)
    d.setheading(d_to_a_angle)
    
    # now march forward one step of length epsilon
    a.forward(epsilon)
    b.forward(epsilon)
    c.forward(epsilon)
    d.forward(epsilon)
    
    # Every so often pause and draw connector lines between all four bugs
    if nCycles % int(s/6.1) == 0:
        box.up()
        box.setpos(a)
        box.setheading(a.towards(b))
        box.down()
        box.pencolor(a.pencolor())
        box.forward(box.distance(b))
        box.up()
        box.setpos(b)
        box.setheading(b.towards(c))
        box.down()
        box.pencolor(b.pencolor())
        box.forward(box.distance(c))
        box.up()
        box.setpos(c)
        box.setheading(c.towards(d))
        box.down()
        box.pencolor(c.pencolor())
        box.forward(box.distance(d))
        box.up()
        box.setpos(d)
        box.setheading(d.towards(a))
        box.down()
        box.pencolor(d.pencolor())
        box.forward(box.distance(a))
    
    # Since a has taken one step: Add the length of that step to the distance accumulator for bug a
    a_cumulative += epsilon

    # Keep track of how many times the while True loop has run
    nCycles += 1
    
    # The turtle function .distance() tells us how far apart the two turtles are
    #   If this proves to be less than 'close_distance' we say the bugs are done walking
    if a.distance(b) < close_distance: break

    # If the program has run away into an infinite loop this will eventually cause it to stop
    if nCycles > 10.0 * s / epsilon: 
        print('breaking owing to program taking too long to finish')
        break

a.hideturtle()
b.hideturtle()
c.hideturtle()
d.hideturtle()
box.hideturtle()

# Now state how many steps we took and how far we went
print(nCycles, 'bugsteps')
print('Distance', "%.4f" % (a_cumulative / s), 'in units of s')
