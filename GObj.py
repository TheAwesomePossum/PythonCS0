'''
Author: Graham Montgomery
Western State Colorado University

This file holds the Graphic objects for the library
'''

# External imports
import threading
import math

# Internal imports
from Globals import *
from Colors import *

class GObj:

    def __init__(self, x, y, color):
        self._lock = threading.Lock()
        self.x = x
        self.y = y
        self.color = color
        self.visible = True
        
    def move(self, xv, yv):
        self.x += xv
        self.y += yv
        
    def setLocation(x, y):
        self.x = x
        self.y = y
    
    def acquire(self):
        self._lock.acquire()
    def release(self):
        self._lock.release()
    def __setattr__(self, item, value):
        if item is "_lock":
            self.__dict__[item] = value
        else:
            self.acquire()
            self.__dict__[item] = value
            self.release()

class Circle(GObj):

    def __init__(self, x, y, color):
        GObj.__init__(self, x, y, color)
        self.radius = 5
        self._type = "Circle"
        
    def draw(self, window):
        if self.visible:
            pygame.draw.circle(window, self.color, (self.x+self.radius, self.y+self.radius), self.radius, 0)
    
    def _getBox(self):
        x = self.x
        y = self.y
        r = self.radius
        return ((x, y),(x+2*r, y+2*r)) 
    
    
class Rectangle(GObj):
    
    def __init__(self, x, y, color):
        GObj.__init__(self, x, y, color)
        self.width = 10
        self.height = 10
        self._type = "Rectangle"
        
    def draw(self, window):
        if self.visible:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
            
    def _getBox(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return ((x, y),(x+w, y+h)) 

class Label(GObj):
    
    def __init__(self, x, y, message):
        GObj.__init__(self, x, y, BLACK)
        self.message = message
        self.fontSize = 15
        self.fontType = None
        
    def draw(self, window):
        if self.visible:
            window.blit(pygame.font.Font(self.fontType, self.fontSize).render(self.message, 1, self.color), (self.x - self.fontSize, self.y - self.fontSize))
 
def collides(obj1, obj2):
    box1 = obj1._getBox()
    box2 = obj2._getBox()
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    w = 0
    h = 0
    if box1[0][0] < box2[0][0]:
        xmin = box1[0][0]
        xmax = box2[0][0]
        w = box1[1][0] - box1[0][0]
    else:
        xmin = box2[0][0]
        xmax = box1[0][0]
        w = box2[1][0] - box2[0][0]
    if box1[0][1] < box2[0][1]:
        ymin = box1[0][1]
        ymax = box2[0][1]
        h = box1[1][1] - box1[0][1]
    else:
        ymin = box2[0][1]
        ymax = box1[0][1]
        h = box2[1][1] - box2[0][1]
    return xmax - xmin < w and ymax - ymin < h
 