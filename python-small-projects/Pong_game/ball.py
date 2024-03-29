from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move

        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # there is some glitch with ball when hitting the bat
        # two type of speedup is used here
        self.movespeed *= 0.09
        self.speedup()

    def recenter(self):
        self.penup()
        self.goto(0, 0)
        self.bounce_x()
        #
        self.movespeed = 0.1
        # self.x_move *= -1
        self.pendown()

    def speedup(self):
        new_speed = self.speed() + 2
        self.speed(new_speed)
