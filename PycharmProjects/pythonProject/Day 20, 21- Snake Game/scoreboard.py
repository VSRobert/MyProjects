from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)   #pentru a il pozitiona in top-centru
        self.color("white")  #pentru ca default scrie negru si am modificat sa fie alb
        self.hideturtle()  #pentru a disparea pin-ul cu sageata/turtle
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center",font=("Arial", 12, "normal"))  # functie de text din turtle module

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 35, "normal"))

