from turtle import Screen, Turtle
import time
from snake import Snake
import random

###🖥️Screen setup🖥️###
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()

###🐍️Snake setup🐍️###
snake = Snake()
###🐍️Snake moves🐍️###
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


























screen.exitonclick()