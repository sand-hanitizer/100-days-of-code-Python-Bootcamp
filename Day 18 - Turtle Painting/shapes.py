import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
colors = ["turquoise", "spring green", "tomato", "orchid","lavender","firebrick","lime","teal","crimson","sienna","gold"]
for i in range(3,11):
    angle = 360/i
    length = 150
    timmy.color(random.choice(colors))
    for r in range(i):
        timmy.forward(length)
        timmy.right(angle)


screen = Screen()
screen.screensize(1500,1500)
screen.exitonclick()
