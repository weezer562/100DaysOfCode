from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
   
    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]
    
    def make_snake(self):
        x_coord = 0.0
        y_coord = 0.0
        for _ in range(0,3):
            new_square = Turtle("square")
            new_square.penup()
            new_square.color("white")
            new_square.setposition(x_coord, y_coord)
            x_coord -= MOVE_DISTANCE   
            self.snake.append(new_square)
            
    def mov(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            
            self.snake[snake_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)