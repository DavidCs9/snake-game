from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0


    def create_scoreboard(self):
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.write("Score: " + str(self.score), False, "center", font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.create_scoreboard()
    
    def score_up(self):
        self.score += 1
        self.update_scoreboard()
    
