import random
from turtle import Turtle, Screen

timmy=Turtle()
colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","Green","wheat"]

directions=[0,90,180,270]
timmy.pensize(10)
timmy.speed("fastest")
timmy.shape("turtle")

def random_color(colors):
    color= random.choice(colors)
    return color

# Challange
'''
for i in range(200):
    turtle.pencolor(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
'''

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color(colors))
        timmy.setheading(timmy.heading() + 10)
        timmy.circle(100)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()


