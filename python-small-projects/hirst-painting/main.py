import turtle
from random import choice

tim = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255.0)
screen.screensize(10,10)
# import colorgram
#
#
# colors = colorgram.extract('img.jpg', 30)
# extracted_color = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color = (r,g,b)
#     extracted_color.append(color)
#
# print(extracted_color)


MY_COLOR = [(249, 228, 17), (235, 251, 244), (212, 13, 9), (198, 13, 36), (229, 228, 6), (196, 70, 21), (33, 90, 188),
            (235, 148, 39), (43, 212, 71), (33, 30, 152), (16, 22, 54), (68, 9, 49), (243, 40, 151), (14, 206, 223),
            (67, 202, 229), (63, 21, 10), (235, 243, 250), (224, 20, 111), (15, 154, 21), (228, 167, 10), (248, 11, 9),
            (98, 75, 9), (245, 59, 16), (223, 140, 202), (69, 240, 159), (10, 97, 62), (6, 38, 33), (70, 218, 156)]


def pic_color():
    global MY_COLOR
    return choice(MY_COLOR)
def circle():

    tim.color(pic_color(), "black")
    tim.dot(20)
    tim.penup()
    tim.fd(50)
    tim.fd(50)
    tim.pendown()
# screen.reset()
#  10 BY 10 Canvas , size of dot = 20 and gap_between_dots = 50
print(tim.pos())
tim.penup()
tim.goto(-350, -290)
tim.pendown()
level_up = 0
go_up = 60
for level in range(11):
    for _ in range(8):
        circle()
    level_up += go_up
    tim.penup()
    tim.goto(-350, -290 + level_up)
    tim.pendown()




screen.exitonclick()
