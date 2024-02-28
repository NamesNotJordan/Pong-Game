
# TODO: create moving paddle
from turtle import Turtle
STRETCH_W = 5
STRETCH_L = 1
class Paddle(Turtle):
    def __init__(self, x, y) -> None:
        self.shape("rectangle")
        self.color('white')
        self.up()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x, y)
        


# Moving
    def up(self):
        self.goto(self.xcor(), self.ycor()+20)
    

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)