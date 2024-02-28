from turtle import Turtle
STRETCH_W = 5
STRETCH_L = 1
class Paddle(Turtle):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x, y)
        


# Moving
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)
    

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)