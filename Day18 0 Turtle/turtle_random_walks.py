import turtle as t
import random

t.pensize(8)
t.shape("square")
t.speed("fastest")


#lists of color for random line color
t.colormode(255)
directions = [0, 90, 180, 270]

r = 0
g = 0
b = 0

def random_color():
    """"function select random number for RGB"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color




#for loops to make a random moves and a random line color
for _ in range (200):
    t.pencolor(random_color())
    t.setheading(random.choice(directions))
    forword = t.forward(random.randint(10, 60))





screen = t.Screen()
screen.exitonclick()