from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(x = 350,y= 0)
        self.setheading(90)




    def up(self):
        self.forward(20)


    def down(self):
        self.backward(20)


