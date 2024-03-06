from turtle import Turtle
from random import choice, randint

COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(choice(COLOR))
        self.goto(250, 0)
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.setheading(180)
        self.all_car = []

    def generate_car(self):
        spawn = randint(-250, 250)
        new_car = Turtle()
        new_car.penup()
        new_car.color(choice(COLOR))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=1.5)
        new_car.setheading(180)
        new_car.goto(350, spawn)

        self.all_car.append(new_car)

    def car_level_up(self):
        self.reset()
        self.car_speed += MOVE_INCREMENT

    def move(self):
        for car_object in self.all_car:
            car_object.forward(self.car_speed)

    def stop_moving(self):
        self.car_speed = 0
