from cs0 import *

window.setColor(BLUE)
window.setCaption("poop nuget mcfart")

charlie = Circle(20, YELLOW)

add(charlie, 321, 114)

start()

count = 0
while(count is not 100):
    if charlie.x > window.width:
        charlie.setLocation(0,0)
    charlie.move(2, 2)
    pause(25)
    count = count + 1

stop()