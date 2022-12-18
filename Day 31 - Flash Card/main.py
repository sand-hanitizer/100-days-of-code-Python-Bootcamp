from tkinter import *
from pandas import DataFrame, read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

title = "French"
word = "WORD"

# --------------------------- READ RANDOM FRENCH WORDS --------------------------------
with open("data/french_words.csv") as file:
    data = read_csv(file)
    french_words = DataFrame.to_dict(data, orient="records")
    print(french_words)


def get_word():
    word_dict = choice(french_words)
    french_word = word_dict["French"]
    meaning = word_dict["English"]


# -------------------------- UI FOR THE FLASH CARD -------------------------------------

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
flashcard_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# Canvas
display_front = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
display_front.create_image(400, 263, image=flashcard_front)
display_front.grid(row=0, column=0, columnspan=2)
display_front.create_text(400, 150, font="Arial 40 italic", text=f"{title}")
display_front.create_text(400, 263, font="Arial 60 bold", text=f"{word}")

# Buttons
correct = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR)
correct.grid(row=1, column=0)
incorrect = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR)
incorrect.grid(row=1, column=1)

window.mainloop()
