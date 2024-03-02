import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()


def up(snake):
    snake.setheading(90)


def down(snake):
    snake.setheading(180)


def left(snake):
    snake.setheading(270)


def right(snake):
    snake.setheading(360)


screen.onkeypress(fun=up, key="Up")
screen.onkeypress(fun=down, key="Down")
screen.onkeypress(fun=left, key="Left")
screen.onkeypress(fun=right, key="Right")
# starting_positions = [(0,0),(-20,0),(-40,0)]
# segments = []

# for position in starting_positions:
#     tim = Turtle("square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(position)
#     segments.append(tim)

game_is_on = True

screen.update()
while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()
    # for seg_num in range(len(segments) -1 , 0 ,-1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)
    # segments[0].left(90)

screen.exitonclick()
