from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=l_paddle.paddle_up)
screen.onkey(key="s", fun=l_paddle.paddle_down)

screen.onkey(key="Up", fun=r_paddle.paddle_up)
screen.onkey(key="Down", fun=r_paddle.paddle_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ball.detect_wall_collision()
    ball.detect_paddle_collisions(right_paddle=r_paddle, left_paddle=l_paddle)

    ball.detect_paddle_miss(scoreboard)

screen.exitonclick()
