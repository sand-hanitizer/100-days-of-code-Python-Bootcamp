import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
colors = ["turquoise", "spring green", "tomato", "orchid"]
for _ in range(20):
    timmy.color(random.choice(colors))
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.screensize(2000,1500)
screen.exitonclick()
