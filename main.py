from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip
import json

FONT_NAME = ("Roboto", 12, "normal")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
data = {}
selection = [letters, numbers, symbols]

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)


def generate_pass():
    global password
    password = []
    for x in range(0, 13):
        chosen_list = choice(selection)
        password.append(choice(chosen_list))

    final_password = ''.join(password)
    pyperclip.copy(final_password)
    passen.insert(0, final_password)


def search():
    try:
        with open("passwords.json", mode="r") as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exist")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"There is no data available for {weben.get()}")
    else:
        try:
            email_disp = data_file[weben.get()]["email"]
            pass_disp = data_file[weben.get()]["password"]
        except KeyError:
            messagebox.showinfo(title="Error", message=f"There is no data available for {weben.get()}")
        else:
            messagebox.showinfo(title="Login information", message=f"Your email/username is: {email_disp} "
                                                               f"\nYour password is: {pass_disp}")
    finally:
        weben.delete(0, END)


def add_deets():
    new_web = weben.get()
    new_email = emailen.get()
    new_pass = passen.get()

    new_data = {
        new_web: {
            "email": new_email,
            "password": new_pass,
        }
    }
    if len(new_web) == 0 or len(new_email) == 0 or len(new_pass) == 0:
        messagebox.showinfo(title="Error", message="One or more field(s) is empty")
    else:
        try:
            with open("passwords.json", mode="r") as file:
                global data
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            data.update(new_data)
            with open("passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)

            weben.delete(0, END)
            passen.delete(0, END)
            emailen.delete(0, END)
            emailen.insert(0, "<Your email here>")
            messagebox.showinfo(title=f"{new_email}", message="Success! \nYour credentials have been saved")


website = Label(text="Website:", font=FONT_NAME)
website.grid(row=1, column=0, sticky="e")
emailuser = Label(text="Email/Username:", font=FONT_NAME)
emailuser.grid(row=2, column=0)
passw = Label(text="Password:", font=FONT_NAME)
passw.grid(row=3, column=0, sticky="e")

weben = Entry(width=33)
weben.grid(row=1, column=1, sticky="w")
weben.focus()
emailen = Entry(width=52)
emailen.grid(row=2, column=1, columnspan=2, sticky="w")
emailen.insert(0, "aadikeshu2305@gmail.com")
passen = Entry(width=33)
passen.grid(row=3, column=1, sticky="w")

addbutton = Button(text="Add", width=44, command=add_deets)
addbutton.grid(row=4, column=1, columnspan=2, sticky="w")
genpass = Button(text="Generate Password", command=generate_pass)
genpass.grid(row=3, column=2, sticky="w")
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()
