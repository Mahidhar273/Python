from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for segments in self.turtle_list:
            segments.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def add_segment(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.turtle_list.append(tim)

    def extend_snake(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for t in range(len(self.turtle_list) - 1, 0, -1):
            x_cor = self.turtle_list[t - 1].xcor()
            y_cor = self.turtle_list[t - 1].ycor()
            self.turtle_list[t].goto(x_cor, y_cor)
        self.head.fd(MOVE_DIST)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
