from turtle import Turtle

FONT=("Courier", 18, "normal")

#defining score class
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.update_score()

#increases score by 1 each time snake eats food
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High score: {self.high_score}", False, "center", FONT)


    def increase_score(self):
        self.score+=1
        self.update_score()


    # def line_for_border(self):
    #     self.goto(-300,270)
    #     self.pendown()
    #     self.fd(600)
    #     self.penup()

#displays game over using write()


    def reset_game(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("data.txt",mode="w") as data:
            data.write(f"{self.high_score}")
        self.score=0
        self.update_score()
