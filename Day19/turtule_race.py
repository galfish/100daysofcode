import turtle
from turtle import Turtle, Screen
import random



#screen setup
screen = Screen()
screen.setup(width=500,height=400)
screen.bgpic("backgrd.gif")

#User input of winnig turtle

is_race_on = False

#lists:
colors = ["green", "violet", "gold", "deep sky blue", "sienna", "black"]
y_posion = [-50, -20, 10, 40, 70, 100]
turtle_list = []


def contiune_game():

    replay = turtle.textinput(title="The Turtle Race", prompt="wont to play again?")
    if replay == "yes":
        global is_race_on
        is_race_on = True
        screen.resetscreen()
        screen.clearscreen()
        screen.bgpic("backgrd.gif")
        game()
    else:
        turtle.bye()


#turtles(1-5):
def game():
    user_bat = turtle.textinput(title="The Turtle Race",
                                prompt="Which turtle will win the race? \nplease select a color \n(green, violet, gold, deep sky blue, sienna, black): ")
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_posion[turtle_index])
        turtle_list.append(new_turtle)

    if user_bat:
        is_race_on = True

    while is_race_on:
        for tim in turtle_list:
            print(tim.xcor())
            if tim.xcor() > 230:
                is_race_on = False
                winnig_color = tim.pencolor()
                if winnig_color == user_bat:
                    print (f"You have won! The {tim.fillcolor()} turtle as won!")
                    turtle.home()
                    contiune_game()
                else:
                    print (f"You have lost! The {tim.fillcolor()} turtle as won!")
                    contiune_game()
        for i in turtle_list:
            i.forward(random.randint(1 ,15))
            i.speed(random.randint(5, 10))


game()


screen.exitonclick()


