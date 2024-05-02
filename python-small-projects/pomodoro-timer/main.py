import math
from tkinter import *
from math import floor


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def action_reset_timer():
    global reps

    window.after_cancel(timer)
    timer_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def action_start_timer():
    global reps
    global work_done

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # for testing
    # work_sec = 5
    # short_break_sec = 1
    # long_break_sec = 3


    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer_label.config(text = "Break" , foreground=RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        timer_label.config(text="Break" , foreground=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work" , foreground=GREEN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(floor(count / 60))
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"



    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count_min == 0:
        canvas.itemconfig(timer_text, text = f"{count_sec}")
    print(count)
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:

        if reps % 2 == 0:
            work_done = math.floor(reps/2)
            tick.config(text=f"{checkmark_text * work_done}")
        action_start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro") #means tomato
window.config(padx=100, pady=50, bg=YELLOW)


checkmark_text = "✔"

canvas = Canvas(width=204  , height=228 , bg=YELLOW , highlightthickness= 0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(102, 112, image = tomato_img)
timer_text = canvas.create_text(102, 130, text='00:00' , fill="white" , font=(FONT_NAME, 35, "bold"))
canvas.grid(column = 1 , row = 1)



#Labels
timer_label = Label(text="Timer", font=(FONT_NAME, 24,"bold"), foreground=GREEN ,background = YELLOW)
timer_label.grid(column = 1, row = 0)

#Button
#calls action() when pressed
start_button = Button(text="START", command=action_start_timer , highlightthickness=0)
start_button.grid(column = 0, row =2)


#Button
#calls action() when pressed
reset_button = Button(text="RESET", command=action_reset_timer)
reset_button.grid(column = 2, row =2)

#Labels
tick = Label(text='', font=(FONT_NAME, 24,"bold"), foreground=GREEN ,background = YELLOW)
tick.grid(column = 1, row = 3)








window.mainloop()


