from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_forward():
    tim.forward(15)
    
def move_backwards():
    tim.back(15)
    
def clear_screen():
    tim.reset()

screen.listen()

screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()