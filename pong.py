"""Simple pong singleplayer built in Python 3 with the turtle module;
Originally made by @TokyoEdTech & customized by @schumann_victor.

The current version of the game in on singleplayer mode. To revert it back to multiplayer, simply change `paddle_a.shapesize(stretch_wid=300)` to `paddle_a.shapesize(stretch_wid=5` and the bouncing `paddle_a.ycor() +- 300` to `paddle_a.ycor() +- 50`. Also, do not forget to change the text to suit a multiplayer environment.
"""

# Environment set up;
import turtle

wn = turtle.Screen()
"""WN functions and properties set the window color, size, and stop it from constantly updating.
This helps with out game framerates & retro feel."""

wn.title("Pong by @schumann_victor")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
"""Turtle class allows us to inherit many properties to graphically customize our game elements.
"""
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=300, stretch_len=1)

paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
"""Written in a way that allows multiplayer if a future patch is necessary.
"""
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
"""Friendly reminder: 'dx' & 'dy' define pixel value of delta. Change with caution.
"""
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Score = 0", align="center", font=("Courier", 10000, "normal"))

# Functions
def paddle_a_up():
    """Assigns y coordinates to custom variable 'y' so we move the paddle_a up.
    """
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    """Assigns y coordinates to custom variable 'y' so we move the paddle_a down.
    """
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    """Assigns y coordinates to custom variable 'y' so we move the paddle_b up.
    """
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    """Assigns y coordinates to custom variable 'y' so we move the paddle_b down.
    """
    y = paddle_b.ycor()
    y -= 40
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

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -.2

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -.2

    # Bouncing
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 300 and ball.ycor() > paddle_a.ycor() - 300:
        ball.dx *= -1.2


    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1.2
