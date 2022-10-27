from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(height=300, width=300)
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles",font=("Arial",16,"bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Helvetica", 16, "italic"))
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=("Helvetica", 16, "italic"))
km_result_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Helvetica", 16, "italic"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km, font=("Helvetica", 16, "italic"))
calculate_button.grid(column=1, row=2)

window.mainloop()
