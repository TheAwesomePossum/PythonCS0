from cs0 import *

setColor(BLUE)
setCaption("hello")

charlie = Oval(20, 40, YELLOW)

add(charlie, 321, 114)

def mouseClick(evt):
    print(str(evt.pos))
    
mouseClickedEvent(mouseClick)

start(thread = False)

count = 0
while(count < 500):
    if charlie.x > window.width:
        charlie.setLocation(0,0)
    charlie.move(2, 2)
    pause(25)
    count = count + 1
    #print(count)

stop()
