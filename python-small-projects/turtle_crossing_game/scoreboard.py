Font = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 230)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=Font)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"GaMe OvEr", align="left", font=Font)
        print("game over")
