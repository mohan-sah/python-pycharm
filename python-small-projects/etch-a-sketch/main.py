# TODO 1; MOVE W

# TODO 2; MOVE BACK S
# TODO 3; TURN LEFT A

# TODO 4; TURN RIGHT D
# TODO 5; CLEAR SCREEN C


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.colormode(255)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")

screen.onkeypress(fun=turn_left, key="a")

screen.onkeypress(fun=turn_right, key="d")

screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
