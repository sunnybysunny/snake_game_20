from turtle import Turtle

# Constant variables
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)



