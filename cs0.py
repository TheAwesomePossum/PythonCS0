'''
Author: Graham Montgomery
Western State Colorado University

This file is the baisic import file for any cs0 project. It will hold some baisic functions for manipulating the world and starting the engine
'''

import time

import Globals as g
import Engine

from Colors import *
from GObj import *

class _Window:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.caption = "Game Window"
        self.color = WHITE
        
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def setCaption(self, caption):
        self.caption = caption
    def setColor(self, color):
        self.color = color

window = _Window()

def add(obj, xPos, yPos):
    obj.x = xPos
    obj.y = yPos
    g.world.add(obj)

def remove(obj):
    g.world.remove(obj)

def start():
    Engine.start(window.width, window.height, window.caption, window.color)
    
def inWindow(obj):
    for gobj in g.world:
        if obj is gobj:
            return True
    return False

def stop():
    Engine.stop()
    
def pause(t):
    time.sleep(t/1000.0)