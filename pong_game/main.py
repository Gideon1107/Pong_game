from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

root = screen.getcanvas().winfo_toplevel()
root.iconbitmap("pong.ico")

game_is_on = True

right_paddle = Paddle((370,0))
left_paddle = Paddle((-370,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #Detect collision with wall and bounce

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with both paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() > -350:
        ball.bounce_x()

    #Detect is right paddle misses the ball
    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()


    # Detect is left paddle misses the ball
    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()