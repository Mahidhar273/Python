import turtle
from turtle import Turtle, Screen
import random
size_of_gap = int(input("Enter the angle: "))

screen = Screen()
timmy = Turtle()
turtle.colormode(255)


def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed(0)


def spiro_kun(gap_size):
    for i in range(int(360 / gap_size)):
        timmy.circle(100)
        timmy.left(gap_size)
        timmy.color(rgb_color())


spiro_kun(size_of_gap)
# turtle.fd(50)
# turtle.tilt(30)
# turtle.fd(50)
# while True:
#     timmy.forward(30)
#     theColor = rgb_color()
#     timmy.color(theColor)
#     timmy.setheading(random.choice(directions))

# i=3
# while i < 10:
#     j = i
#
#     while j > 0:
#         timmy.forward(100)
#         timmy.right(360/i)
#         j -= 1
#     theColor = random.choice(colors)
#     timmy.color(theColor)
#     i += 1

screen.exitonclick()
