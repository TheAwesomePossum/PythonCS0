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

def flipDisplay():
    '''
    this will be the graphics thread
    '''
    while(g.running and g.threadCount is threading.activeCount()):
        g.currentTime = time.time()
        if g.currentTime > g.refreshTime:
            g.window.fill(g.bgcolor)
            world = g.world
            world.acquire()
            for gobj in world.world:
                gobj.acquire()
                gobj.draw(g.window)
                gobj.release()
            world.release()
            g.pygame.display.flip()
            g.refreshTime = g.currentTime + g.deltaTime

GraphicThread = threading.Thread(target=flipDisplay, args=())

def start(width, height, caption, color):
    '''
    Sets up pygame
    Sets up the window
    Starts graphics thread
    '''
    g.pygame.init()
    size = (width, height)
    g.window = g.pygame.display.set_mode(size)
    g.pygame.display.set_caption(caption)
    g.window.fill(color)
    g.bgcolor = color
    g.pygame.display.flip()
    g.running = True
    g.startTime = time.time()
    g.threadCount += 1
    GraphicThread.start()
    
def stop():
    '''
    stops the graphic thread
    '''
    g.running = False
    GraphicThread.join()
