import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
user_inp = screen.textinput(title="Make Bet", prompt="Choose a colour")

screen.setup(width=500, height=400)

# def move_forward():
#     tim.fd(25)
#
#
# def move_back():
#     tim.back(25)
#
#
# def move_right():
#     tim.right(5)
#
#
# def move_left():
#     tim.left(5)
#
#
# def curve_up():
#     tim.left(5)
#     tim.forward(25)
#
#
# def curve_down():
#     tim.right(5)
#     tim.forward(25)
#
#
# def clear_kun():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="Up", fun=curve_up)
# screen.onkey(key="Down", fun=curve_down)
# screen.onkey(key="c", fun=clear_kun)
# screen.listen()
is_race_on = False
turtle_list = []
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for index in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(-235, -150+index*50)
    turtle_list.append(tim)

if user_inp:
    is_race_on = True

while is_race_on:
    for turtle_kun in turtle_list:
        turtle_kun.forward(random.randint(0, 20))
        if turtle_kun.xcor() > 230:
            is_race_on = False
            if user_inp == turtle_kun.pencolor():
                print("you won")
            else:
                print(f"You lost, the winner is {turtle_kun.pencolor()}")


screen.exitonclick()


