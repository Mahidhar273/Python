from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open("F:/Profile/SnakeGame/score.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("F:/Profile/SnakeGame/venv/Scripts/score.txt", mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.score_write()

    def score_up(self):
        self.score += 1
        self.score_write()

