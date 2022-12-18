from tkinter import *

word = "WORD"
meaning = "MEANING"
BACKGROUND_COLOR = "#B1DDC6"


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
display_front.create_text(400,150,font="Arial 40 italic",text=f"{word}")
display_front.create_text(400,263,font="Arial 60 bold",text=f"{meaning}")

# Buttons
correct = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR)
correct.grid(row=1, column=0)
incorrect = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR)
incorrect.grid(row=1, column=1)

window.mainloop()
