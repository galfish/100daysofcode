from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forword():
    tim.forward(10)
def turn_right():
    tim.right(25)
def turn_left():
    tim.left(25)
def move_back():
    tim.back(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()

in.py

screen.listen()

screen.onkey(key="w", fun=move_forword)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

