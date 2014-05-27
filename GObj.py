'''
Author: Graham Montgomery
Western State Colorado University

This file holds the Graphic objects for the library
'''
import threading

from Globals import *

class GObj:

    def __init__(self):
        self._lock = threading.Lock()
        
    def acquire(self):
        self._lock.acquire()
    def release(self):
        self._lock.release()
    def __setattr__(self, item, value):
        self.acquire()
        if self.__dict__.hasitem(item):
            dict.__setattr__(self, item, value)
        else:
            self. __setitem__(item, value)
        self.release()

class Circle(GObj):

    def __init__(self, x, y, radius):
        GObj.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius