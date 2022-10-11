from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("indigo")
        self.speed("fastest")
        self.reset_position()

    def reset_position(self):
        x_cor = randint(-290, 290)
        y_cor = randint(-290, 240)
        self.goto(x_cor, y_cor)
