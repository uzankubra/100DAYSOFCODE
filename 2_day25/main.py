import pandas as pd
from turtle import Turtle, Screen

screen=Screen()
turtle=Turtle()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]

df=pd.read_csv("50_states.csv")
all_states=df.state.to_list()

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another states name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
