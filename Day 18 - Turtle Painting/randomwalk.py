import random
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.width(5)
timmy.speed(9)
timmy.hideturtle()

dirc = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(50):
    timmy.color(random_color())
    timmy.forward(40)
    timmy.right(random.choice(dirc))

screen = turtle.Screen()
screen.exitonclick()
