from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self, io):
        super().__init__()

        self.io = io
        self.saved_scores = self.io.read_file()
        self.high_score = self.saved_scores[1]
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Updates score on screen"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.io.write_to_file(self.score, self.high_score)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()
