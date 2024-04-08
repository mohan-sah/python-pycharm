import tkinter as tk


firstclick = True

def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        entry.delete(0, "end") # delete all the text in the entry


root = tk.Tk()

label = tk.Label(root, text="User: ")
label.pack(side="left")

entry = tk.Entry(root, bd=1)
entry.insert(0, 'Enter your user name...')
entry.bind('<FocusIn>', on_entry_click)
entry.pack(side="left")

root.mainloop()