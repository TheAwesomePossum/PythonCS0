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

class _data:
    def __init__(self):
        pass

window = _data()

window.width = 500
window.height = 500
window.caption = "Game Window"
window.color = WHITE

def add(obj, xPos, yPos):
    obj.x = xPos
    obj.y = yPos
    g.world.add(obj)

def remove(obj):
    g.world.remove(obj)

def start():
    Engine.start(window.idth, window.height, window.caption, window.color)

def stop():
    Engine.stop()
    
def pause(t):
    time.sleep(t/1000.0)