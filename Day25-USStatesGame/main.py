import os
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=500)

us_image = "blank_states_img.gif"

screen.addshape(us_image)
screen.tracer(0)
turtle.shape(us_image)


def pin_state(state):

    pin = turtle.Turtle()
    pin.hideturtle()
    pin.penup()
    pin.goto(int(state.x.iloc[0]), int(state.y.iloc[0]))
    pin.color("black")
    pin.write(state.state.item())


def write_data(missing_list):
    new_data = pd.DataFrame(missing_list)
    new_data.to_csv("state_to_learn")


state_data = pd.read_csv("50_states.csv")
list_state_data = state_data.state.to_list()
correct_guesses = []

continue_guessing = True
while continue_guessing:
    screen.update()
    box_title = f"{len(correct_guesses)}/50 States Correct"

    answer_state = screen.textinput(title=box_title, prompt="What's another state name?")

    # Handle cancel button
    if answer_state is not None:
        answer_state = answer_state.title()

    if answer_state == "Exit" or answer_state is None:
        missing_states = [state for state in list_state_data if state not in correct_guesses]
        write_data(missing_states)
        continue_guessing = False
        break

    if answer_state in list_state_data:
        correct_guesses.append(answer_state)
        pin_state(state_data[state_data.state == answer_state])

turtle.mainloop()



