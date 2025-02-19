from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as highscore_doc:
            self.highscore = int(highscore_doc.read())
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-50, 280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}       HighScore: {self.highscore}")


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-30, 0)
        self.write("Game over.")

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore_doc:
                highscore_doc.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
