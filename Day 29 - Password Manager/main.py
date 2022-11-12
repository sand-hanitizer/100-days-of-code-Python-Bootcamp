import tkinter
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    with open("data.txt","a") as file:
        file.write(f"{website} | {user} | {password}")




# ---------------------------- UI SETUP ------------------------------- #

# display
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# password manager logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# website entry
website_label = Label(text="Website",bg="white")
website_label.grid(row=1, column=0)
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# username entry
username_label = Label(text="Email/Username", bg="white")
username_label.grid(row=2, column=0)
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0,"ananya@email.com")

# password
password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="EW")

gen_pass = Button(text="Generate Password", highlightthickness=0, bg="white", fg="#024B30")
gen_pass.grid(row=3, column=2, sticky="EW")

# add button
add = Button(text="Add", width=39, highlightthickness=0, bg="white", fg="#024B30", command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW")

# keep screen on
window.mainloop()
