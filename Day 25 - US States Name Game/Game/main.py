import turtle

screen = turtle.Screen()
screen.title("US States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer = screen.textinput(title="Guess the State", prompt="What's the state's name?")

turtle.mainloop()
