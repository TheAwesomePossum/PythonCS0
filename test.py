from cs0 import *

g.WindowCaption = "Collide Test"
WW = g.WindowWidth = 1000
WH = g.WindowHeight
xv = 2
yv = 0

l=Label(0,0, "Hello World")

start()

add(l)

for i in range(1000):

    pause(10)

print("Stopping")
stop()
