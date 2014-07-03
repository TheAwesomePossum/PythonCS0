from cs0 import *

setColor(BLUE)
setCaption("hello")

charlie = Oval(20, 40, YELLOW)

add(charlie, 321, 114)

def mouseClick(evt):
    print(str(evt[0]))
    
mouseClickedEvent(mouseClick)

start()

count = 0
while(count is not 1000):
    if charlie.x > window.width:
        charlie.setLocation(0,0)
    charlie.move(2, 2)
    pause(25)
    count = count + 1

stop()
