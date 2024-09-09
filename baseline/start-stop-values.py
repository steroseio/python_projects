# range function first input specifies the number to start at, and the
# second input determines the number to stop at.
from turtle import *

for i in range(1, 50): # note the stop number is exclusive, so the last value used is actually 49
    forward(5 * i)
    left(90)
    
bye()

# the third input to range is step size - i.e. how many numbers to jump between each loop
for i in range(5, 50, 5):
    forward(i) # 5, 10, 15, 20, 25, 30, 35, 40, 45
    left(90)
    
bye()

# negative step sizes can also be used
for i in range(100, 0, -5):
    forward(i)
    left(90)
    
bye()

# here we are using turtle function to draw a flower with petals of varying sizes. This draws
# larger petals last on top of the smaller petals. Reverse the range parameters to draw the 
# larger petals first and the smaller ones on top, like 'for i in range(200, 0, -10)

color('black', 'magenta') # line color black, fill color magenta

def left_turn(length):          # define function expecting a argument we'll call length
    for i in range(10):         # for loop counting 0 thru 9 (so 10x)
        forward(length / 10)    # go forward length argument / 10
        left(9)                 # turn turtle 9 deg to the left

def petal(size):                # define function expecting a argument we'll call size
    begin_fill()                # turtle function to fill shapes
    left_turn(size)             # call left_turn function with a argument set for size
    left(90)                    # turn left 90 deg
    left_turn(size)             # call left turn function with a argument set for size
    left(90)                    # turn left 90 deg
    end_fill()                  # turtle function to stop filling shapes

for i in range(0, 200, 10):     # for loop 0, 10, 20, 30, 40, 50 ... 190
    petal(i)                    # call petal function - i is defined as 0, 10, 20 etc
    right (360/10)              # turn turtle right 36 deg after every loop of the petal function
    
bye()

# define some functions that include arguments. This is a function that takes no arguments
width(2)                    # set the pen width to 2

def circle():               # define a function with no arguments called circle
    penup()                 # built in function to lift pen (do not draw)
    forward(50)             # move forward 50 px (right from centre)
    pendown()               # built in function to place pen (draw)
    left(90)                # turn left 90 deg
    for i in range(60):     # for loop to run 0, 1, 2, 3, 4 .. 59
        forward(5)          # draw 5 px in faced direction
        left(6)             # turn left 6 deg
    right(90)               # loop has ended - turn right 90 deg
    penup()                 # built in function to lift pen (do not draw)
    back(50)                # move back 50 px - now in centre of circle that was drawn
    pendown()               # built in function to place pen (draw)
    
circle()                    # call the function - a circle will be drawn
bye()

# in the above function we would update L-59 from '5' to a different number in order to draw
# a different sized circle. Instead, we can use a function argument
def circle(size):           # define a function with a required param called circle
    penup()                 
    forward(size*30 / 3.14) # calculates radius of circle based half of circumference / Pi
    pendown()
    left(90)
    for i in range(60):
        forward(size)       # argument will be specificed when calling the function later
        left(6)
    right(90)
    penup()
    back(200)
    pendown()

circle(10)                  # draw a circle with size of 10 - param 'size' replaced with argument 10
circle(20)                  # 'size' replaced with 20 = bigger circle
bye()

print("-------------------------------------------------------------------------------------")
print("Circumference of the circle is 'size * 60'")
print("Diameter of the circle is Circumference / Pi (3.14)")
print("Radius of the circle is half the circumference")
print("In the calc above we have divided half of the circumference by Pi to get the radius")
print("This allows the turtle to maintain a consistent centre regardless of circle size")
print("-------------------------------------------------------------------------------------")
