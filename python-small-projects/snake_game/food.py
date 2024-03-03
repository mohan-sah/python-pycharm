from turtle import Turtle,Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.shapesize(0.4,0.2)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280,240)
        random_y = random.randint(-280,240)
        self.goto(random_x,random_y)
        self.showturtle()
        self.a = (random_x,random_y)
        print(self.a)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# screen  = Screen()
#
#
# screen.exitonclick()


