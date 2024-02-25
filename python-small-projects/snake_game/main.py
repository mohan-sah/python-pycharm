import time
from turtle import Turtle,Screen
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    segments.append(tim)

game_is_on = True
#pus
screen.update()
while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(10)
        time.sleep(0.25)












screen.exitonclick()

