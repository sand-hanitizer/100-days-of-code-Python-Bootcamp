from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
colors = ["turquoise", "spring green", "tomato", "orchid"]
for i in range(4):
    timmy.color(colors[i])
    timmy.left(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
