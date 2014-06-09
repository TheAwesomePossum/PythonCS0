from cs0 import *

g.WindowCaption = "Bouncy Ball"
WW = g.WindowWidth = 1000
WH = g.WindowHeight
xv = 1
yv = 2

start()

c = Circle(5, 5, RED)
add(c)

for i in range(2000):
    c.move(xv,yv)
    if c.x >= WW or c.x <= 0:
        xv *= -1
        c.move(xv, 0)
    elif c.y >= WH or c.y <= 0:
        yv *= -1
        c.move(0, yv)
    pause(40)

print("Stopping")
stop()
