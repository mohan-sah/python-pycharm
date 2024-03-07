import random
import time
from turtle import Turtle, Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()

screen.title("Turtle_crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate cars for level

    cars.generate_car()
    cars.move()

    # reach finish line
    if player.is_at_finish_line():
        scoreboard.level_up()
        scoreboard.update_level()
        player.reset_player()
        cars.car_level_up()


    # if car collide with player : game over
    for car in cars.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            cars.stop_moving()


screen.exitonclick()
