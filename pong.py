"""Simple pong built in Python 3 with the turtle module;
Originally made by @TokyoEdTech & customized by @schumann_victor.
"""

# Environment set up;
import turtle
import os

wn = turtle.Screen()
# WN functions and properties set the window color, size, and stop it from constantly updating. This helps with our game framerates & retro feel.

wn.title("Pong by @schumann_victor")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
# Friendly reminder: 'dx' & 'dy' define pixel value of delta. Change with caution.
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .05
ball.dy = .05

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up(): # Assigns y coordinates to custom variable 'y' so we move the paddle_a up.
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)

def paddle_a_down(): # Assigns y coordinates to custom variable 'y' so we move the paddle_a down.
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Ball Movement;
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay pongBounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay pongBounce.wav&")

    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = -.05
        ball.dy = -.05
        os.system("aplay pongDeath.wav&")

    if ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = .05
        ball.dy = .05
        os.system("aplay pongDeath.wav&")

    # Bouncing
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1.2
        os.system("aplay pongBounce.wav&")


    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1.2
        os.system("aplay pongBounce.wav&")
