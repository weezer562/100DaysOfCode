from turtle import Turtle

LEFT_PADDLE = "left"
RIGHT_PADDLE = "right"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score(self.l_score, self.r_score)

    def update_point(self, paddle):
        if paddle == LEFT_PADDLE:
            self.l_score += 1
        elif paddle == RIGHT_PADDLE:
            self.r_score += 1

        self.write_score(self.l_score, self.r_score)

    def write_score(self, l_score, r_score):
        self.clear()
        self.goto(-100, 200)
        self.write(l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(r_score, align="center", font=("Courier", 80, "normal"))
