import turtle
import pandas as pd
import string

screen = turtle.Screen()
screen.title("US States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

states_data = pd.DataFrame(pd.read_csv("50_states.csv"))
states_name = states_data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer = str(screen.textinput(title=f"Guess the State,{len(guessed_states)}/50", prompt="What's the state's name?"))
    answer = string.capwords(answer)

    if answer == "End":
        missing = [x for x in states_name if x not in guessed_states]
        data = pd.DataFrame(missing)
        data.to_csv("states_missed.csv")
        break

    text = turtle.Turtle()
    for x in states_name:
        if answer == x:
            row = states_data[states_data["state"] == answer]
            if answer not in guessed_states:
                guessed_states.append(answer)
            print(row)
            location = (int(row['x']), int(row['y']))
            text.hideturtle()
            text.penup()
            text.goto(location)
            text.write(f"{answer}", font=("Arial", 12, "normal"))

