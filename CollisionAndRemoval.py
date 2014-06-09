from cs0 import *

g.WindowCaption = "Collide Test"
WW = g.WindowWidth = 1000
WH = g.WindowHeight
xv = 2
yv = 0

start()

c = Circle(15, 260, BLUE)
p = Rectangle(5, 250, RED)
p.height = 25
add(p)
add(c)

for i in range(1000):
    c.move(xv,yv)
    if c.x >= WW or c.x <= 0:
        xv *= -1
        c.move(xv, 0)
    elif c.y >= WH or c.y <= 0:
        yv *= -1
        c.move(0, yv)
    if p is not None:
        if collides(c, p):
            remove(p)
            p = None
            xv *= -1
    pause(20)

print("Stopping")
stop()
