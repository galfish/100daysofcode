import turtle as t


t.shape("turtle")
t.color("violet")


def dashed_line():
    for x in range(25):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

def dashed_left():
    t.left(90)
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    t.left(90)

def dashed_right():
    t.right(90)
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    t.right(90)

for i in range(10):
    dashed_line()
    dashed_left()
    dashed_line()
    dashed_right()





screen = t.Screen()
screen.exitonclick()