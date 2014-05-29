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

g.WindowWidth = 500
g.WindowHeight = 500
g.WindowCaption = "Game Window"
g.WindowColor = WHITE

def add(obj):
    g.world.add(obj)

def remove(obj):
    g.world.remove(obj)

def start():
    Engine.start(g.WindowWidth, g.WindowHeight, g.WindowCaption, g.WindowColor)

def stop():
    Engine.stop()
    
def pause(t):
    time.sleep(t/1000.0)