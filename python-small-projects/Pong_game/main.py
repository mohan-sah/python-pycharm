import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

screen.tracer(0)
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(1)

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    # detect collision top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        print(ball.movespeed)


    # detect ball goes out of bound
    if ball.xcor() > 400:
        ball.recenter()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.recenter()
        scoreboard.r_point()


screen.exitonclick()
