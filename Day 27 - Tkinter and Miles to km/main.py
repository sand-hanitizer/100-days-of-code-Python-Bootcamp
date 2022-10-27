from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20, width=200, height=200)

empty_label = Label(text="None", fg="#f0f0f0")
empty_label.grid(column=0, row=0)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles",font=("Helvetica",16,"italic"))
miles_input.grid(column=2, row=0)

is_equal_label = Label(text="is equal to",font=("Helvetica",16,"italic"))
miles_input.grid(column=0, row=1)

km_result_label = Label(text="0",font=("Helvetica",16,"italic"))
miles_input.grid(column=1, row=1)

km_label = Label(text="km",font=("Helvetica",16,"italic"))
miles_input.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km,font=("Helvetica",16,"italic"))
miles_input.grid(column=1, row=2)


window.mainloop()
