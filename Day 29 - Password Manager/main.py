import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# display
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# password manager logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# website entry
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# username entry
username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

# password
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password")
gen_pass.grid(row=3, column=2)

# add button
add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)

# keep screen on
window.mainloop()
