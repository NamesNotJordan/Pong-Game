
# TODO: Create screen

# TODO: Create another Paddle
# TODO: Collisions
# TODO: Create moving ball
# TODO: detect paddle miss
from turtle import Screen
from paddle import Paddle
# Setting Up Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)


# Create Paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)


# Gameplay
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
