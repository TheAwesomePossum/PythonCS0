'''
Author: Graham Montgomery
Western State Colorado University

This file is the baisic import file for any cs0 project. It will hold some baisic functions for manipulating the world and starting the engine
'''

import time
import random

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
    if  (not g.multithreading) and g.running:
        #print("fliping Display")
        Engine.flipOnce()
    time.sleep(t/1000.0)

####### Engine Starting/Stoping

def start(thread=True):
    #print(thread)
    Engine.start(window, thread)

def stop():
    Engine.stop()
    
    
######## Event Handeling

def mouseClickedEvent(handle):
    Events.addMouseClickedEvent(handle)
    
def mouseReleasedEvent(handle):
    Events.addMouseReleasedEvent(handle)
    
def mouseMovedEvent(handle):
    Events.addMouseMovedEvent(handle)
    
def keyPressedEvent(handle):
    Events.addKeyPressedEvent(handle)
    
def keyReleasedEvent(handle):
    Events.addKeyReleasedEvent(handle)

def mouseDraggedEvent(handle):
    Events.addMouseDraggedEvent(handle)


###### Extra functions
def objectAt(pos):
    p = Rectangle(1,1,WHITE)
    for obj in g.world:
        if collides(obj,p):
            return obj
    return None
        
def moveForward(obj):
    world = g.world.world
    for i in range(len(world)):
        if world[i] is obj and i is not 0:
            world[i], world[i-1] = world[i-1], world[i]
            return
    
def moveBackward(obj):
    world = g.world.world
    for i in range(len(world)):
        if world[i] is obj and i is not 0:
            world[i], world[i-1] = world[i-1], world[i]
            return
        
def sendToFront(obj):
    world = g.world.world
    for i in range(len(world)):
        if world[i] is obj and i is not 0:
            for j in reversed(range(1,i+1)):
                world[j], world[j-1] = world[j-1], world[j]
            return 
        
def sendToBack(obj):
    world = g.world.world
    for i in range(len(world)):
        if world[i] is obj and i is not 0:
            for j in range(i,len(world)):
                world[j], world[j+1] = world[j+1], world[j]
            return 

def randomDouble():
    return random.random()

def randomInt(min, max = None):
    if max is None:
        return int(random.random() * (min - .01))
    else:
        return int(random.random() * ((max +.99) - min)) - min