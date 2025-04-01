from turtle import Turtle
import random
#inheritance. Food class inherits from turtle class.
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("lightgreen")
        self.speed(0)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-258, 258)
        random_y = random.randint(-258, 258)
        self.goto(random_x, random_y)