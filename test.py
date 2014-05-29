from cs0 import *

start()

c = Circle(5,5)

for i in range(0,100):
    c.move(1, 1)
    pause(.1)

print("Stopping")
stop()
