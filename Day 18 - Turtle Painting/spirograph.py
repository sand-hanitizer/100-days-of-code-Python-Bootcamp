import random
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)
timmy.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw(gap):
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.seth(timmy.heading() + gap)


draw(int(input()))
screen = turtle.Screen()
screen.exitonclick()
