import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.shape("turtle")

colors = [(188, 19, 46), (243, 232, 66), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173),
          (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63),
          (36, 44, 110), (77, 174, 96), (214, 68, 49)]
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setposition(-250, -250)
fd = 50
n = 10
for _ in range(n):
    for _ in range(n):
        tim.dot(20, random.choice(colors))
        tim.forward(fd)

    y = tim.ycor() + fd
    x = tim.xcor() - n * fd
    tim.setposition(x, y)

screen = turtle.Screen()
screen.exitonclick()
