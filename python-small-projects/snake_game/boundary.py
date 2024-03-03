from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        self.speed("slowest")

    def makeboundary(self):
        for _ in range(4):
            self.forward(580)
            self.right(90)


