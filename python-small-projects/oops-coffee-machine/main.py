#
# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.pen(fillcolor="coral", pencolor="red", pensize=10)
# timmy.fd(300)
# timmy.speed(10)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# timmy.shape("turtle")
#
#
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle" , "Charmander"])
table.add_column("Type", ["Electric" , "Water" , "Fire"])
table.align = "l"
table.valign = "b"
table.add_row(["Chalizard","Fire"])


print(table)



