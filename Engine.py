'''
Author: Graham Montgomery
Western State Colorado University

This file contains all the graphic logic for the project. 
'''

# External Imports
import threading # used to create graphics thread(perhaps one day move this to graphics chip)
import time

# Internal Imports
import Globals as g # project global variables
import Events



def flipDisplay():
    '''
    this will be the graphics thread
    '''
    again = True
    stopFlag = False
    while(g.threadCount is threading.activeCount() and again):
        flipOnce()
        g.clock.tick(g.deltaTime)
        if not g.running:
            stopFlag = True
        if stopFlag:
            again = False

def flipOnce():
    Events.updateEvents()
    g.window.fill(g.world.color)
    world = g.world
    world.acquire()
    for gobj in world.world:
        gobj.acquire()
        gobj.draw(g.window)
        gobj.release()
    world.release()
    g.pygame.display.flip()
    

GraphicThread = threading.Thread(target=flipDisplay, args=())

def start(world, thread):
    '''
    Sets up pygame
    Sets up the window
    Starts graphics thread
    '''
    g.threading = thread
    size = (world.width, world.height)
    g.window = g.pygame.display.set_mode(size)
    g.pygame.display.set_caption(world.caption)
    g.window.fill(world.color)
    g.pygame.display.flip() 
    g.startTime = time.time()
    g.running = True
    if thread:     
        g.threadCount += 1
        GraphicThread.start()
    
def stop():
    '''
    stops the graphic thread
    '''
    g.running = False
    if g.multithreading:
        GraphicThread.join()
        Events.eraseEvents()
    while True:
        Events.updateEvents()
        g.clock.tick(g.deltaTime)
