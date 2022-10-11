from turtle import Screen
import time
from Snake import Snake
from food import Food
from Scoreboard import Score
scoreboard = Score()
food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake_kun Game")
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.reset_position()
        snake.extend_snake()
        scoreboard.score_up()
    # Detecting wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detecting collision with tail
    for segment in snake.turtle_list[1:]:
        # if segment == snake.head:
        #     pass
        # el
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
