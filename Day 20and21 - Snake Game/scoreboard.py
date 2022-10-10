from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=("Arial", 24, "normal"))
