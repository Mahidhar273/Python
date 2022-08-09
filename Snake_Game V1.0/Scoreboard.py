from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.score_write()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)