import turtle as t
import random

tim = t.Turtle()

colors = ["spring green", "hot pink", "dodger blue", "yellow", "sandy brown"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)



for shape_side_n in range (3, 15):
    draw_shape(shape_side_n)
    tim.color(random.choice(colors))



screen = t.Screen()
screen.exitonclick()