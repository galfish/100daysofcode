import turtle as t
import random

t.pensize(1)
t.shape("turtle")
t.speed("fastest")

#for random color line:
t.colormode(255)
def random_color():
    """"function select random number for RGB"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

"""My try:
for _ in range (90):
    t.pencolor(random_color())
    t.circle(100)
    t.penup()
    t.circle(0, 5, 10)
    t.pendown()
    """

#Angela solution:
def draw_spirpgraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirpgraph(5)



screen = t.Screen()
screen.exitonclick()