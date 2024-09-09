from turtle import *

# define a custom function
def left_turn():
    for i in range(10):
        forward(15)
        left(9)

# call the function
left_turn()

# functions are re-usable once defined, we could call the function a further
# 3 times in order to draw a full circle
left_turn()
left_turn()
left_turn()

# nested functions are functions that can be built out of other functions
hideturtle()
color('black', 'magenta')

def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn
    left(90)
    end_fill()

def flower():
    for i in range(5):
        petal()
        right(360/5)

flower()
    