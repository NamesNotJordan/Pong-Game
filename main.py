
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


#Controls
screen.listen()
screen.onkey(right_paddle.go_up,"i")
screen.onkey(right_paddle.go_down, "k")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down, "s")

# Gameplay
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
