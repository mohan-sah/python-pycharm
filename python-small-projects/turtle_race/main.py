import random
from turtle import Turtle, Screen

#addition 1 ; what if the user want to change the bet in middle of race,
# maybe giving them at 1/4 of race another chance to change the betted player





screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)


is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# def create_turtle(colors):
#     goup = 50
#     for color in colors:
#         myturtle = Turtle(shape="turtle")
#         myturtle.penup()
#         myturtle.color(color)
#         myturtle.goto(-230, -150+goup)
#         goup +=40
#     return myturtle
# create_turtle(colors)
def turtle_step(turtle_name):
    steps = random.randint(0, 10)
    turtle_name.fd(steps)


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")

    new_turtle.penup()
    new_turtle.color("black", colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Place Your bet", prompt="Which turtle will win the race ? Enter a color : ")
print(user_bet)
print(all_turtles)
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.color()[1]
            if winning_turtle == user_bet:
                print(f"you 've won !  The {winning_turtle} turtle is the winner .")
            else :
                print(f"you 've lost !  The {winning_turtle} turtle is the winner .")
        turtle_step(turtle)

screen.exitonclick()
