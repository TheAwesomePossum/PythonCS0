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

def add(obj, xPos=0, yPos=0):#------------------- 7/30 modified with defaults 
    window.add(obj, xPos, yPos)

def remove(obj):
    window.remove(obj) #----------------------- 7/30 (obj) was missing
    
def removeAll(): #------------------------------ 8/1 we need this, removes all objects from the window
    window.world = []

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
def objectAt(pos): #--------------- several changes here
    #needed to specify the location of the Rectangle, otherwise it's at 0,0
    #p = Rectangle(1,1,WHITE, pos[0], pos[1]) #---don't know why this doesn't work
    p = Rectangle(1, 1, WHITE)                #---but these 2 statements
    p.setLocation(pos[0], pos[1])             #---make it work
    for obj in g.world.world: #------------ missing last .world I think
        if type(obj) is not Label and collides(obj,p): #can't collide with a Label
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

#-------------------------------------- my random functions
def randomSeed(val):
    random.seed(val)

def randomInt(min, max = None): #clever, I didn't know about None
    #returns random int in range [min, max] or [0, min]
    if max is None:
        return random.randint(0, min)
    else:
        return random.randint(min, max)
    
def randomDouble(min, max = None):
    #return random double in range [min, max) or [0, min)
    if max is None:
        return (min)*random.random()
    else:
        return (max-min)*random.random() + min
    
def randomBoolean():
    v = randomInt(1, 2)
    if v == 1: return True
    else: return False
        
        
def randomProbability(p):
    r = randomDouble(1)
    if r < p: return True
    else: return False