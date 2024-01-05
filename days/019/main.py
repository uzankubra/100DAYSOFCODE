

from turtle import Turtle, Screen
import random

is_race_on=True

screen=Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for i in range(len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on= True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won. Congratulations! The {winning_color} is the winner! ")
            else:
                print(f"You've lost. The {winning_color} is the winner! ")
        random_distance= random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()
