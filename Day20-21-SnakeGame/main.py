import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_LENGTH = 600

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_LENGTH)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control Setup
screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.grow()
        
    # Border detection collision
    game_is_on = snake.border_check(SCREEN_WIDTH, SCREEN_LENGTH)
    
    # Detect collision with self tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()
