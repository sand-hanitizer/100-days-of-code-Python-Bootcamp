from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.level_update()

    def game_over(self):
        self.goto(-60, 0)
        self.write(arg="GAME OVER", font=FONT)

    def level_update(self):
        self.goto(-250, 230)
        self.write(arg=f"LEVEL: {self.level}", font=FONT)

