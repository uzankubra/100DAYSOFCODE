
import os
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

from snake import Snake
import time
from food import Food
from turtle import Turtle, Screen
from scoreboard import ScoreBoard

food=Food()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard=ScoreBoard()
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()



    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on= False
        scoreboard.game_over()

    # detect collision with tail
        # if head collides with any segment in the tail:
            # trigger game over
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()








screen.exitonclick()