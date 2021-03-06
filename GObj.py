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
from Constants import *

import Engine

class GObj:

    def __init__(self, color, x, y):
        self._lock = threading.Lock()
        self.cx = 0
        self.cy = 0
        self.x = x
        self.y = y
        self.color = color
        self.visible = True
        
    def move(self, xv, yv):
        self.x += xv
        self.y += yv
        
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getLocation(self):
        return (self.x, self.y)
    
    def getX(self): #------------------------------- 7/30 added
        return self.x
   
    def getY(self): #------------------------------- 7/30 added
        return self.y    

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color

    def setVisible(self, val):
        self.visible = val
    def getVisible(self):
        return self.visible
    
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
    def __add__(self, obj):
        if type(obj) is GComp:
            obj.objs.append(self)
            return obj
        elif isinstance(obj, GObj):
            obj.cx = obj.x
            obj.x = 0
            obj.cy = obj.y
            obj.y = 0
            self.cx = self.x
            self.x = 0
            self.cy = self.y
            self.y = 0
            return GComp(self, obj)
            
class GComp(GObj):
    
    def __init__(self, obj1, obj2): 
        GObj.__init__(self, WHITE, 0, 0)
        self.objs = [obj1,obj2]
        
    def move(self, xv, yv):
        self.x += xv
        self.y += yv
        self.updateQualities();      
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.updateQualities();
    def setVisible(self, val):
        self.visible = val
        self.updateQualities();
    def updateQualities(self):
        for obj in self.objs:
            obj.x = self.x + obj.cx
            obj.y = self.y + obj.cy
            obj.setVisible(self.visible)
    def getWidth(self):
        maxX = 0
        minX = 0
        for obj in self.objs:
            if obj.x >= maxX:
                maxX = obj.x
            elif obj.x <= minX:
                minX = obj.x
        return maxX-minX
    def getHeight(self):
        maxY = 0
        minY = 0
        for obj in self.objs:
            if obj.y >= maxY:
                maxY = obj.y
            elif obj.y <= minY:
                minY = obj.y
        return maxY-minY
            
    def draw(self, window):
        for obj in self.objs:
            obj.draw(window);
            
    def __add__(self, obj):
        if type(obj) is GComp:
            self.objs += obj.objs
        elif isinstance(obj, GObj):
            obj.cx = obj.x
            obj.x = 0
            obj.cy = obj.y
            obj.y = 0
            self.objs.append(obj)
        return self

    def _getBox(self):
        maxX = 0
        maxY = 0
        minX = 0
        minY = 0
        for obj in self.objs:
            if obj.x >= maxX:
                maxX = obj.x
            elif obj.x <= minX:
                minX = obj.x
            if obj.y >= maxY:
                maxY = obj.y
            elif obj.y <= minY:
                minY = obj.y
        return ((minX, minY), (maxX,maxY))
        
class Circle(GObj):

    def __init__(self, diam, color, x = 0, y = 0):
        GObj.__init__(self, color, x, y)
        self.diam = diam
        self._type = "Circle"

    def setDiameter(self, diam):
        self.diam = diam
    def getDiameter(self):
        return self.diam
        
    def draw(self, window):
        if self.visible:
            pygame.draw.circle(window, self.color, (int(self.x+self.diam/2), int(self.y+self.diam/2)), int(self.diam/2), 0)
    
    def _getBox(self):
        x = self.x
        y = self.y
        r = self.diam/2
        return ((x, y),(x+2*r, y+2*r))
    
class Square(GObj): #----------------------------- 7/30 add this class
                    #----------------------------- haven't checked it thoroughly
    def __init__(self, width, color, x = 0, y = 0):
        GObj.__init__(self, color, x, y)
        self.width = width
        self.height = width
        self._type = "Square"
 
    def setWidth(self, width):
        self.width = width
        
    def getWidth(self):
        return self.width
        
    def draw(self, window):
        if self.visible:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)
            
    def _getBox(self):
        x = self.x
        y = self.y
        w = self.width
        return ((x, y),(x+w, y+w))

class Oval(GObj):

    def __init__(self, width, height, color, x = 0, y = 0):
        GObj.__init__(self, color, x, y)
        self.width = width
        self.height = height
        self._type = "Oval"

    def setSize(self, width, height):
        self.width = width
        self.height = height
    def setWidth(self, width): #----------------- 7/30
        self.width = width
    def setHeight(self, height): #---------------- 7/30
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
        
    def draw(self, window):
        if self.visible:
            pygame.draw.ellipse(window, self.color, (self.x, self.y, self.width, self.height), 0)
    
    def _getBox(self):
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return ((x, y),(x+w, y+h))
    
    
class Rectangle(GObj):
    
    def __init__(self, width, height, color, x = 0, y = 0):
        GObj.__init__(self, color, x, y)
        self.width = width
        self.height = height
        self._type = "Rectangle"

    def setSize(self, width, height):
        self.width = width
        self.height = height
    def setHeight(self, height): #-------------- 7/30
        self.height = height
    def setWidth(self, width): #---------------- 7/30
        self.width = width
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
        
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
    
    def __init__(self, size, color, message, x = 0, y = 0):
        GObj.__init__(self, color, x, y)
        self.message = message
        self.fontSize = size
        self.fontType = None

    def setFontSize(self, fontSize): #-------- 7/30 changed name
        self.fontSize = fontSize
    def getFontSize(self):              #---------- 7/30 changed name
        return self.fontSize

    def setText(self, message):
        self.message = message
    def getText(self): #------------------ 7/30 added
        return self.message    
    
    def draw(self, window):
        if self.visible:
            window.blit(pygame.font.Font(self.fontType, self.fontSize).render(self.message, 1, self.color), (self.x, self.y))
 
def collides(obj1, obj2):
    if obj1 is None or obj2 is None or not world.inWorld(obj1) or not world.inWorld(obj2):
        return False
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
 
