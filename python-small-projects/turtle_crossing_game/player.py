from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
INCR_DISTANCE_TRAVEL = 5


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line_y = FINISH_LINE_Y
        self.player_speed = MOVE_DISTANCE

    def up(self):
        self.forward(self.player_speed)

    def finish_line(self):
        if self.ycor() > self.finish_line_y:
            self.player_speed += INCR_DISTANCE_TRAVEL
            return True

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

