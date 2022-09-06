from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.fd(30)


def move_bd():
    tim.bk(30)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(fun=move_fd, key="w")
screen.onkey(fun=move_bd, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=clear, key='c')
screen.exitonclick()
