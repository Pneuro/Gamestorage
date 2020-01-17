import turtle as t
import random
    
t.color('red')
t.bgcolor('black')
t.speed(10)
while True:
    
    
    colors = ['red', 'green', 'blue', 'white', 'magenta', 'yellow']
    
    
    change=random.choice(colors)
    
    
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
    next()
    fill()