"""Simple pong built in Python 3 with the turtle module;
Originally made by @TokyoEdTech & customized by @schumann_victor.
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
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
"""Written in a way that allows multiplayer if future patch is necessary.
"""
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=300, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Functions
def paddle_a_up():
    """Assigns y coordinates to custom variable 'ycor'.
    """
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")


# Main game loop;
while True:
    wn.update()
