import turtle as t
import random

t.color('red')
t.bgcolor('black')
t.speed(10)


bumper_r = t.Turtle()
bumper_r.speed(0)
bumper_r.shape('square')
bumper_r.color("red")
bumper_r.shapesize(stretch_wid=5, stretch_len=.5)
bumper_r.penup()
bumper_r.goto(350, 0)

bumper_l = t.Turtle()
bumper_l.speed(0)
bumper_l.shape('square')
bumper_l.color("red")
bumper_l.shapesize(stretch_wid=5, stretch_len=.5)
bumper_l.penup()
bumper_l.goto(-350, 0)

while True:

    colors = ['red', 'green', 'blue', 'white', 'magenta', 'yellow']

    change = random.choice(colors)

    def draw():
        t.color(change)
        t.lt(45)
        t.forward(100)
        t.circle(50, 180, 25)
        t.rt(90)
        t.circle(50, 180, 25)
        t.forward(100)

    def next():
        t.color(change)
        t.lt(45)
        t.circle(90)

    def fill():
        t.fd(12)
        t.rt(12)
        draw()

    draw()
    next()
    fill()
