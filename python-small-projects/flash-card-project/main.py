from tkinter import *

import pandas
import pandas as pd
from random import choice



BACKGROUND_COLOR = "#B1DDC6"


current_card = {}
to_learn = {}
# Read the data from the french_words.csv file in the data folder.
try:
    data_frame = pd.read_csv(filepath_or_buffer="./data/word_to_learn.csv")

except FileNotFoundError:
    print("Previously learnt word file is not found. loading french_words file.")
    orignal_data = pd.read_csv(filepath_or_buffer="./data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")


# dict_french_word = {row.French:row.English for (index,row) in data_frame.iterrows()}
# print(dict_french_word)
#{'partie': 'part', 'histoire': 'history'} to [{'French': 'partie', 'English': 'part'}]

print(to_learn)
current_card = {}
mastered =[]



#Pick a random French word/translation and put the word into the flashcard.
# Every time you press the ❌ or ✅ buttons,
# it should generate a new random word to display.
def next_card():
    global  current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    print(current_card["French"], current_card["English"])
    canvas.itemconfig(card_title, text ="French", fill = "black")
    canvas.itemconfig(card_word, text =  current_card["French"], fill = "black")
    canvas.itemconfig(canvas_image, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English" , fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"] , fill  = "white")
    canvas.itemconfig(canvas_image, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    mastered.append(current_card)

    data_of_to_learn = pandas.DataFrame(to_learn)
    data_of_to_learn.to_csv("data/word_to_learn.csv", index=False)

    data_of_mastered = pandas.DataFrame(mastered)
    data_of_mastered.to_csv("data/Already_learned.csv" , index=False)


    print(len(to_learn))
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file = "./images/card_front.png")
card_back_img = PhotoImage(file ="./images/card_back.png")
canvas_image= canvas.create_image(400,263,image = card_front_img)
card_title = canvas.create_text(400,150,text="Title" , font=("ariel", 40, "italic"))
card_word = canvas.create_text(400,256,text="word" , font=("ariel", 60, "bold"))

canvas.config(bg = BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row = 0, column = 0 , columnspan =2 )

cross = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross,command=next_card, highlightthickness= 0 )
unknown_button.grid(row = 1, column = 0)

check = PhotoImage(file ="./images/right.png")
known_button = Button(image=check, command= is_known , highlightthickness= 0)
known_button.grid(row = 1, column =1)

next_card()

window.mainloop()

