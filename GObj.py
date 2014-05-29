'''
Author: Graham Montgomery
Western State Colorado University

This file holds the Graphic objects for the library
'''

# External imports
import threading

# Internal imports
from Globals import *
from Colors import *

class GObj:

    def __init__(self):
        self._lock = threading.Lock()
        
    def acquire(self):
        self._lock.acquire()
    def release(self):
        self._lock.release()
    def __setattr__(self, item, value):
        if item is "_lock":
            self.__setitem__(item, value)
        else:
            self.acquire()
            if self.__dict__.hasitem(item):
                dict.__setattr__(self, item, value)
            else:
                self.__setitem__(item, value)
            self.release()

class Circle(GObj):

    def __init__(self, x, y, radius):
        GObj.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = RED
        self.visible
        
    def move(self, xv, yv):
        self.x += xv
        self.y += yv
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius, 0)