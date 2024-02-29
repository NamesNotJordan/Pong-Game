from turtle import Turtle
SPEED = 10
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = SPEED
        self.y_move = SPEED


    def center_court(self):
        self.goto(0, 0)
        self.bounce_x()


    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1
    

    def bounce_x(self):
        self.x_move *= -1
    
    def speed_up(self):
        self.x_move += 5
        self.y_move += 5