# aim : to learn how to read and understand documentation.
import random
from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
terry = Turtle()
screen = Screen()

import heroes
from random import choice

print(heroes.gen())

tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(4):
#     for _ in range(4):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)


# some wierd symbol it is making
# it can be a good logo

# for i in range(3,10):
#
#     for i in range(3,10):
#         angle = 360 / i
#         tim.forward(40)
#         tim.right(angle)
list_of_turtle_color = ["yellow", "gold", "orange", "red", "maroon", "violet",
                        "magenta", "purple", "navy", "blue", "skyblue", "cyan",
                        "turquoise", "lightgreen", "green", "darkgreen", "chocolate",
                        "brown", "black", "gray"]


# TODO 2 : did it . Finally the shapes i wanted

# def move(sides):
#     for move in range(sides):
#         tim.right(angle)
#         tim.forward(40)
# print(choice)
# for i in range(3,11):
#     angle = 360 / i
#     tim.pencolor(choice(list_of_turtle_color))
#     move(i)


# TODO 3 : draw at random and random color

def color_no():
    return random.randint(1, 254)


direction = [360, 90, 180, 270]

screen.colormode(255.0)
tim.speed(1000)
tim.pensize(10)
for _ in range(100):
    # r = float(color_no())
    # g = float(color_no())
    # b = float(color_no())
    r = color_no()
    g = color_no()
    b = color_no()
    tim_direction = choice(direction)
    print(r,g,b)
    tim.pencolor((r, g, b))

    tim.setheading(tim_direction)
    tim.heading()
    tim.fd(15)


screen.exitonclick()
