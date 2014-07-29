from cs0 import *

setColor(BLUE)
setCaption("hello")

charlie = Circle(10, RED, 0,0) + Circle(10, YELLOW, 5,5) #+ Rectangle(10,15, AQUA,0, 10)
#print(type(charlie))
#add(sam, 326, 119)
#charlie += sam 
charlie += Rectangle(10,15, AQUA,0, 10)
add(charlie, 321, 114)

def mouseClick(evt):
    print(str(evt))
    
mouseClickedEvent(mouseClick)
mouseReleasedEvent(mouseClick)
#mouseMovedEvent(mouseClick)
mouseDraggedEvent(mouseClick)
keyPressedEvent(mouseClick)
keyReleasedEvent(mouseClick)

start(thread = False)
#start()

count = 0
while(count < 500):
    if charlie.x > window.width:
        charlie.setLocation(0,0)
    charlie.move(2, 2)
    pause(25)
    count = count + 1
    #print(count)

stop()
