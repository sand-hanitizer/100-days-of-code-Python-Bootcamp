from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet!", prompt="Choose a turtle to bet on, Enter your color: ")

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            win = turtle.pencolor()
            if user_bet == win:
                print(f"You've won! The winning turtle is {win}")
            else:
                print(f"You've lost! The winning turtle is {win}")

        dist = random.randint(0, 10)
        turtle.forward(dist)

screen.exitonclick()
