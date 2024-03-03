from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-20, 250)
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.reprint()
        self.update_score()

    def reprint(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("gAmE OvEr", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.reprint()
