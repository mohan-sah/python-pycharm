import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tim = turtle.Turtle()


# To get (x,y) of particular click.
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
def show_on_map(answer_state_name, x, y):
    tim.shapesize(0.4, 0.4)
    tim.penup()
    tim.shape("circle")
    tim.goto(x, y)
    tim.write(f"{answer_state_name}", font=("Arial", 8, "normal"))


states = pd.read_csv("50_states.csv")
state_names = states["state"].to_list()

correct_answer = 0
all_answered = True
answered_list = []
missed_list = []
while all_answered:

    answer_state = screen.textinput(title=f"{correct_answer}/50 Guess the State",
                                    prompt="What's another state's name? ").lower()

    for name in state_names:
        # print(name, states[states.state == f"{name}"].x, states[states.state == f"{name}"].y)
        if answer_state == "exit":
            all_answered = False
            missed_list = [state for state in state_names if state.lower() not in answered_list]
            df = pd.DataFrame(missed_list)
            df.to_csv("states_to_learn.csv")
            break

        if name.lower() == answer_state:
            current_state = states[states.state == name]

            if answer_state not in answered_list:
                answered_list.append(answer_state)
                correct_answer += 1
                show_on_map(str(name), current_state.x.item(), current_state.y.item())
                if correct_answer == 50:
                    all_answered = False  # means game finished
                    print("YOU WON")
                    print("Correctly answered all 50 states")

            else:
                correct_answer += 0

# states_to_learn.csv  contain names user may want to look.


#
# turtle.mainloop()
