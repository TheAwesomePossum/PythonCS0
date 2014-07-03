'''
Author: Graham Montgomery
Western State Colorado University

This file is the baisic import file for any cs0 project. It will hold some baisic functions for manipulating the world and starting the engine
'''

import time

import Globals as g
g.pygame.init()
import Engine
import Events

from Colors import *
from GObj import *

window = g.world
  
###### GUI Editing 

def inWindow(obj):
    return window.inWorld(obj)

def add(obj, xPos, yPos):
    window.add(obj, xPos, yPos)

def remove(obj):
    window.remove

def setCaption(message):
    window.setCaption(message)

def setWidth(width):
    window.setWidth(width)
def setHeight(height):
    window.setHeight(height)
def setSize(width, height):
    window.setSize(width, height)

def setColor(color):
    window.setColor(color)
    
def pause(t):
    time.sleep(t/1000.0)

####### Engine Starting/Stoping

def start():
    Engine.start(window)

def stop():
    Engine.stop()
    
    
######## Event Handeling

def mouseClickedEvent(handle):
    Events.addMouseClickedEvent(handle)
