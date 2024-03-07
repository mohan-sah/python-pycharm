from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-20, 250)
        self.score = 0
        with open("highscore.txt") as highscore_file:
            content = highscore_file.read()
            self.highscore = int(content)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.reprint()
        self.update_score()

    def reprint(self):
        self.clear()
        self.write(f"Score = {self.score}  High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore_file:
                highscore_file.write(f"{self.highscore}")
        self.score = 0
        self.reprint()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("gAmE OvEr", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.reprint()
