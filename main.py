
# TODO: Collisions
# TODO: detect paddle miss
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
# Setting Up Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)

# Create Paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Ball
ball = Ball()
#Controls
screen.listen()
screen.onkey(right_paddle.go_up,"i")
screen.onkey(right_paddle.go_down, "k")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down, "s")

# Gameplay
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Wall Collision
    if abs(ball.ycor()) > 280:
        ball.bounce_y()
    
    # Paddle collsion
    if (ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50) and abs(ball.xcor()) > 340:
        ball.bounce_x()
    
    # Goal
    if abs(ball.xcor()) > 350:
        ball.center_court()
        ball.bounce_x()

screen.exitonclick()
