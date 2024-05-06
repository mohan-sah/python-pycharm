import json
from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_generator = PasswordGenerator()

print(password_generator.password_list)
def action_generate():
    entry_password.delete(0,END)
    temp = password_generator.generate()
    copy(temp)
    entry_password.insert(END, temp)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# in file data.txt
def action_save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        should_save = False
        messagebox.showinfo(title="CANNOT BE SAVED" , message="textbox not filled")
    else:
    #     should_save = messagebox.askokcancel(title=f"{website}", message=f"Details submitted : \n Email : {email}\n Password : {password}\n click ok to save")
    # if should_save:
        data = None
        try:
            with open("data.json" , "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:

            with open("data.json", "w") as file:
                json.dump(new_data,file , indent=4)
                print(data)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                print(data)
        finally:
            # emptying fields
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
#title : Password Manager
#width: 200, padding : 20, Height : 200

window = Tk()

window.title('Password Manager')
window.config(padx=20 , pady=20)

canvas = Canvas(width=200, height=200 )
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column = 1, row = 0)

#Labels - website
label_website = Label(text="Website :")
label_website.grid(column = 0, row = 1)

#Labels - email/username
label_email = Label(text="Email/Username :")
label_email.grid(column = 0, row = 2)

#Labels-password
label_password = Label(text="Password :")
label_password.grid(column = 0, row = 3)

#Entries - website
entry_website = Entry(width=25 )
entry_website.focus()
entry_website.grid(column = 1, row =1 )

#Entries - email
entry_email = Entry(width=44)
entry_email.insert(END , "mohansah944@gmail.com")
entry_email.grid(column = 1, row =2  ,columnspan = 2)

#Entries - password
entry_password = Entry(width=25)
entry_password.grid(column = 1, row =3)

#Button - generate
#calls action() when pressed
button_generate_password = Button(text="Generate Password", command=action_generate , width=15)
button_generate_password.grid(column = 2, row = 3)

#Button - search
def action_search():
    print("do something")
    website = entry_website.get()
    email = 'NOT FOUND'
    password = "NOT FOUND"
    with open("data.json", "r") as file:
        data = json.load(file)
        for i,j in data.items():
            if i.lower() == website.lower():
                email  = data[i]["email"]
                password = data[i]["password"]
        messagebox.showinfo(title=website, message= f"email : {email} \n password : {password}")



#calls action() when pressed
button_generate_password = Button(text="Search", command=action_search , width=15)
button_generate_password.grid(column = 2, row =1)

#Button - add
#calls action() when pressed
button_add = Button(text="Add", command=action_save , width=30)
button_add.grid(column = 1, row = 4 , columnspan  = 2)












window.mainloop()


