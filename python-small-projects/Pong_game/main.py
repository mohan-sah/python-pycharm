from turtle import Turtle,Screen
from paddle import Paddle
from paddle2 import Paddle2



screen = Screen()


screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")

screen.tracer(0)
paddle1 = Paddle()
paddle2 = Paddle2()
screen.tracer(1)



screen.listen()
screen.onkeypress(fun=paddle1.up, key="Up")
screen.onkeypress(fun=paddle1.down, key="Down")
screen.onkeypress(fun=paddle2.up, key="w")
screen.onkeypress(fun=paddle2.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
















screen.exitonclick()