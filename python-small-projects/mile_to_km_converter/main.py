



from tkinter import *

window = Tk()
window.minsize(width=600 , height=400)
window.title("CONVERTER: MILES TO KM")
window.config(padx=100, pady=100)


# label, is equal to  = 1,0
label1 = Label(text= "is equal to ")
label1.grid(row = 1,column = 0)


# label, miles = 0,2
label2 = Label(text="Miles ")
label2.grid(row = 0,column = 2)


# label, Km  = 1,2
label2 = Label(text="Km ")
label2.grid(row = 1,column = 2)

# input , num = 0,1
input_box =  Entry(width=30)
input_box.insert(END, string= "some number")
input_box.focus()
input_box.grid(row = 0,column = 1)

# display , num = 1,1
input_box2 = Entry(width=30)
input_box.insert(END, string= "result in km")
input_box.grid(row = 1,column = 1)


# button , calculate =  2,1
button  = Button(text="click to convert")
button.grid(row = 2, column = 1)










window.mainloop()

