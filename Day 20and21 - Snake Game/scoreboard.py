from turtle import Turtle

with open("data.txt", "r") as file:
    HIGHSCORE = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()

    def reset_scoreboard(self):
        if self.score > int(HIGHSCORE):
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", "r") as file:
            HIGHSCORE = file.read()
        self.write(f"Score: {self.score} High Score: {HIGHSCORE}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
