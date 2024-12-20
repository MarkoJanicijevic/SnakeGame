from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-20, 280)
        self.write(f"Score: {self.score}")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}")

    def game_over(self):
        self.goto(-30, 0)
        self.write("Game over.")
