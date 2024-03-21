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
        """Create starting Snake"""
        x_coord = 0.0
        y_coord = 0.0
        for _ in range(0, 3):
            self.add_segment(x_coord, y_coord)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.make_snake()
        self.head = self.snake[0]

    def move(self):
        """Move Snake segments as one"""
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()

            self.snake[snake_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def border_check(self, x_coord, y_coord, scoreboard):
        """Check if snake reached a screen edge"""
        x = x_coord / 2 - 20
        y = y_coord / 2

        if self.head.xcor() > x or self.head.xcor() <= -y:
            scoreboard.reset()
            self.reset()

        if self.head.ycor() > x or self.head.ycor() < -y:
            scoreboard.reset()
            self.reset()

    def add_segment(self, x_coord, y_coord):
        """Add segment to Snake"""
        x_coord += MOVE_DISTANCE
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.setposition(x_coord, y_coord)
        self.snake.append(new_square)

    def grow(self):
        """Grow the snake"""
        x = self.snake[-1].xcor()
        y = self.snake[-1].ycor()

        self.add_segment(x, y)

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
