# import colorgram, turtle
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
# color_kun = []
# color_san = colorgram.extract('paint.jpg', 30)
# for _ in color_san:
#     r = _.rgb.r
#     b = _.rgb.b
#     g = _.rgb.g
#     new_color = (r, g, b)
#     color_kun.append(new_color)
#
# print(color_kun)
color_chan = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]
tim = Turtle()
screen = Screen()
tim.speed(0)
tim.penup()
tim.setpos(-200, -200)
for _ in range(10):
    for i in range(10):
        tim.pendown()
        num = random.choice(color_chan)
        tim.dot(20, num)
        tim.penup()
        tim.fd(50)
    tim.setposition(-200, -200 + 50*_)

screen.exitonclick()
