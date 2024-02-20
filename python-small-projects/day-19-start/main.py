from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)

def move_forward():
    tim.forward(10)


screen.listen()

screen.onkey(fun=move_forward, key="space")



















screen.exitonclick()
