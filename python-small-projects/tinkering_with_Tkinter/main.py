# import tkinter OR
from tkinter import *

window = Tk()
window.title("GUI PROGRAM")
window.minsize(width=500,height=300)

# *args for arguments where * is important.all arguments are in tuple form
# which then can be looped through.

# def add(*args):
#     for n in args:
#         print(n)
#
# add(n1 = 5, n2 = 3)
# add(2,3,4,5,6)


# label
my_label = Label(text="I am a Label", font=("Ariel", 24,"bold"))

# # passing value to dict as it is a **kwargs OR pass as keyword argument
# my_label["text"] = "new text"
my_label.config(text=" New text")
my_label.pack()



# button
def button_clicked():
    text = input.get()
    my_label.config(text=text)
    my_label.pack()
    print("i got clicked")


button = Button(text = "click me" , command=button_clicked)
button.pack()

# Entry

input = Entry(width= 15)
input.pack()










window.mainloop()