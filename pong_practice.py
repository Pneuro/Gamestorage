import turtle
import os

win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

################################################################################################
############################## Score ###########################################################
################################################################################################

score_l = 0
score_r = 0

################################################################################################
############################## Bumpers ###########################################################
################################################################################################
# Left Bumper
bumper_l = turtle.Turtle()
bumper_l.speed(0)
bumper_l.shape('square')
bumper_l.color("red")
bumper_l.shapesize(stretch_wid=5, stretch_len=.5)
bumper_l.penup()
bumper_l.goto(-350, 0)


# Right Bumper
bumper_r = turtle.Turtle()
bumper_r.speed(0)
bumper_r.shape('square')
bumper_r.color("red")
bumper_r.shapesize(stretch_wid=5, stretch_len=.5)
bumper_r.penup()
bumper_r.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left Player: 0 Right Player: 0", align="center",
          font=('Courier', 24, 'normal'))

# Function


def bumper_l_up():
    y = bumper_l.ycor()
    y += 20
    bumper_l.sety(y)


def bumper_l_down():
    y = bumper_l.ycor()
    y -= 20
    bumper_l.sety(y)


def bumper_r_up():
    y = bumper_r.ycor()
    y += 20
    bumper_r.sety(y)


def bumper_r_down():
    y = bumper_r.ycor()
    y -= 20
    bumper_r.sety(y)


# Keybindings
win.listen()
win.onkeypress(bumper_l_up, "w")
win.onkeypress(bumper_l_down, "s")

win.onkeypress(bumper_r_up, "o")
win.onkeypress(bumper_r_down, "l")


# Main game Loop

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay Aquatic_Snare.aif& ")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay Aquatic_Snare.aif& ")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Left Player: {} Right Player: {}".format(score_l, score_r), align="center",
                  font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        pen.clear()
        pen.write("Left Player: {} Right Player: {}".format(score_l, score_r), align="center",
                  font=('Courier', 24, 'normal'))

    # # Paddle Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bumper_r.ycor() + 40 and ball.ycor() > bumper_r.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay Aquatic_Snare.aif& ")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bumper_l.ycor() + 40 and ball.ycor() > bumper_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay Aquatic_Snare.aif& ")
