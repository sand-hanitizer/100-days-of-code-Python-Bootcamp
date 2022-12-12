import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

from pyperclip import copy

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    password_entry.delete(0, END)
    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = username_entry.get()
    pass_word = password_entry.get()
    new_data = {
        website: {
            "username": user,
            "password": pass_word
        }
    }

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showwarning(title="Warning", message="Do not leave the fields empty.")
    else:
        with open("data.json", "r") as file:
            # Read old data
            data = json.load(file)
            # Update old data with new data
            data.update(new_data)

        with open("data.json", "w") as file:
            # Put all that back in data file
            json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_label = Label(text="Website", bg="white")
website_label.grid(row=1, column=0)
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# username entry
username_label = Label(text="Email/Username", bg="white")
username_label.grid(row=2, column=0)
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "ananya@email.com")

# password
password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="EW")

gen_pass = Button(text="Generate Password", highlightthickness=0, bg="white", fg="#024B30", command=generate_password)
gen_pass.grid(row=3, column=2, sticky="EW")

# add button
add = Button(text="Add", width=39, highlightthickness=0, bg="white", fg="#024B30", command=save)
add.grid(row=4, column=1, columnspan=2, sticky="EW")

# keep screen on
window.mainloop()
