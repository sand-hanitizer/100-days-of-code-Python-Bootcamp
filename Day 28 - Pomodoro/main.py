import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec % 10 == count_sec:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Method")
window.config(padx=100, pady=50, bg=YELLOW)

# timer heading
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
timer_label.config(font=(FONT_NAME, 35, "normal"))
timer_label.grid(column=1, row=0)

# tomato bg
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# start button
start_button = Button(command=start_timer, text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0)
reset_button.grid(column=2, row=2)

# checkmark
check = Label(text=CHECKMARK, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check.grid(column=1, row=3)

window.mainloop()
