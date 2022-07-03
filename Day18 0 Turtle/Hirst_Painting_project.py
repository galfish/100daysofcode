import turtle as t
import random as r
drawing_area = t.Screen()
#drawing_area.setup(width=750, height=500)
t.colormode(255)

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
              (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


def draw_random_dots():
    # loops number_of_dots times
    for _ in range(100):
        t.pencolor(color_list[r.randint(0, 29)])
        # moves to the random position
        t.penup()
        t.goto(r.randint(-500,0),r.randint(0,500))
        t.pendown()
        # Dot color

        # creates a dot
        t.dot(30)

draw_random_dots()


screen = t.Screen()
screen.exitonclick()