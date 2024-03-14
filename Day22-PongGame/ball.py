from turtle import Turtle

COLLISION_SURFACE_WALL = 0
COLLISION_SURFACE_PADDLE = 1
RESET = 1
LEFT_PADDLE = "left"
RIGHT_PADDLE = "right"


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def detect_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce(COLLISION_SURFACE_WALL)

    def detect_paddle_collisions(self, right_paddle, left_paddle):
        if self.distance(right_paddle) < 50 and self.xcor() > 320 or self.distance(
                left_paddle) < 50 and self.xcor() < -320:
            self.bounce(COLLISION_SURFACE_PADDLE)

    def detect_paddle_miss(self, scoreboard):
        if self.xcor() > 380:
            self.reset_position()
            scoreboard.update_point(LEFT_PADDLE)

        if self.xcor() < -390:
            self.reset_position()
            scoreboard.update_point(RIGHT_PADDLE)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce(RESET)

    def bounce(self, surface):
        # wall
        if surface == 0:
            self.y_move *= -1
        # paddles
        elif surface == 1:
            self.x_move *= -1

        self.move_speed *= 0.9
