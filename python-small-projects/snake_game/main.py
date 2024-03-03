import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
from boundary import Boundary

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

boundary = Boundary()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
# starting_positions = [(0,0),(-20,0),(-40,0)]
# segments = []

# for position in starting_positions:
#     tim = Turtle("square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(position)
#     segments.append(tim)

game_is_on = True
#ch
screen.update()
while game_is_on:

    screen.update()
    time.sleep(0.25)
    snake.move()
    boundary.makeboundary()
    if snake.head.distance(food) < 15:  # collision
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        pass
    #if head collide with any segment in the tail :
        #trigger game_over

    # for seg_num in range(len(segments) -1 , 0 ,-1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)
    # segments[0].left(90)

screen.exitonclick()
