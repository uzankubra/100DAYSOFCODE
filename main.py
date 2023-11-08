
from turtle import Turtle, Screen

turtle=Turtle()

turtle.shape("turtle")
turtle.color("green")

# Challange 1 : draw a square
'''
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
'''

# Challange 2 : jumping

'''
for i in range(10):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

    turtle.forward(10)
'''
# Challange 3 : draw a few models

colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SeaGreen"]
def shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

import random

for side_number in range(3,11):
    turtle.color(random.choice(colors))
    shape(side_number)




screen = Screen()
screen.exitonclick()


