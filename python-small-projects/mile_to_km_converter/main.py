



from tkinter import *

window = Tk()
window.minsize(width=200 , height=150)
window.title("CONVERTER: MILES TO KM")
window.config(padx=100, pady=100)

firstclick = True
def miles_to_km():
    """convert miles num to km num"""

    miles = float(miles_input_box.get())
    km = round(miles * 1.609,2)
    print(f"{km} and {miles}")
    km_input_box.delete(0, "end")
    km_input_box.insert(0,f"{km}")


def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        miles_input_box.delete(0, "end") # delete all the text in the entry





# label, is equal to  = 1,0
is_equal_label = Label(text= "is equal to ")
is_equal_label.grid(row = 1,column = 0)



# label, miles = 0,2
miles_label = Label(text="Miles ")
miles_label.grid(row = 0, column = 2)


# label, Km  = 1,2
km_label = Label(text="Km ")
km_label.grid(row = 1, column = 2)

# input , num = 0,1
miles_input_box =  Entry(width=20)
miles_input_box.insert(END, string="These many")
miles_input_box.bind('<FocusIn>', on_entry_click)
miles_input_box.grid(row = 0, column = 1)

# display , num = 1,1
km_input_box = Entry(width=20)
km_input_box.insert(END, string="that much in ")
km_input_box.grid(row = 1, column = 1)


# button , calculate =  2,1
button  = Button(text="click to convert", command= miles_to_km)
button.grid(row = 2, column = 1)










window.mainloop()

