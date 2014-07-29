'''
Author: Graham Montgomery
Western State Colorado University

This constructs the concurency safe world list
'''

import threading

from Colors import *

class World:
    
    def __init__(self):
        self._lock = threading.Lock()
        self.world = []
        self.width = 500
        self.height = 500
        self.caption = "Game Window"
        self.color = WHITE
        
    def acquire(self):
        self._lock.acquire()
    def release(self):
        self._lock.release()

    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def setSize(self, width, height):
        self.width = width
        self.height = height
        
    def setCaption(self, caption):
        self.caption = caption
    def setColor(self, color):
        self.color = color
        
    def add(self, obj, xPos, yPos):
        obj.setLocation(xPos, yPos)
        self.world.append(obj)
        print(self.world)
    def remove(self, obj):
        self.world.remove(obj)
        
    def inWorld(self, obj):
        for gobj in self.world:
            if obj is gobj:
                return True
            return False
