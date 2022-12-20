from tkinter import *
from pandas import DataFrame, read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
french_words = {}
word_dict = {}

# --------------------------- READ RANDOM FRENCH WORDS --------------------------------
try:
    with open("data/words_to_learn.csv") as file:
        data = read_csv(file)
except FileNotFoundError:
    with open("data/french_words.csv") as file:
        data = read_csv(file)
finally:

    french_words = DataFrame.to_dict(data, orient="records")
    print(french_words)


def get_word():
    global flip_timer
    window.after_cancel(flip_timer)
    global word_dict,word,meaning
    word_dict = choice(french_words)
    word = word_dict["French"]
    meaning = word_dict["English"]
    display_front.itemconfig(display_word, text=f"{word}", fill="#000000")
    display_front.itemconfig(display_title, text="French", fill="#000000")
    display_front.itemconfig(display_image, image=flashcard_front)
    flip_timer = window.after(3000, func=change_card)


def is_known():
    global word
    french_words.remove(word_dict)
    words_to_learn = DataFrame(french_words)
    words_to_learn.to_csv("data/words_to_learn.csv",index=False)
    get_word()


# ----------------------------------- FLASHCARD TIMER ---------------------------------
def change_card():
    display_front.itemconfig(display_image, image=flashcard_back)
    global meaning
    display_front.itemconfig(display_word, text=f"{meaning}", fill="#FFFFFF")
    display_front.itemconfig(display_title, text="English", fill="#FFFFFF")


# -------------------------- UI FOR THE FLASH CARD -------------------------------------

# window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# flipping the card
flip_timer = window.after(3000, func=change_card)

# Images
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# Canvas
display_front = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
display_image = display_front.create_image(400, 263, image=flashcard_front)
display_front.grid(row=0, column=0, columnspan=2)
display_title = display_front.create_text(400, 150, font="Ariel 40 italic", text="Language")
display_word = display_front.create_text(400, 263, font="Ariel 60 bold", text="WORD")

# Buttons
correct = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
correct.grid(row=1, column=0)
incorrect = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_word)
incorrect.grid(row=1, column=1)

# get word
get_word()

# ----------------------------------- Window Loop ------------------------
window.mainloop()
