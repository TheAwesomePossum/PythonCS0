'''
Author: Graham Montgomery
Western State Colorado University

This file contains all the graphic logic for the project. 
'''

# External Imports
import threading # used to create graphics thread(perhaps one day move this to graphics chip)
import time

# Internal Imports
from Globals import * # project global variables

def flipDisplay():
    '''
    this will be the graphics thread
    '''
    while(running):
        currentTime = time.time()
        if currentTime > refreshTime:
            #print "Updating window"
            refreshTime = currentTime + deltaTime

GraphicThread = threading.Thread(target=flipDisplay, args=())

def start(width, height, caption, color):
    '''
    Sets up pygame
    Sets up the window
    Starts graphics thread
    '''
    pygame.init()
    size = (width, height)
    Globals.window = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    g.win.fill(color)
    pygame.display.flip()
    running = True
    startTime = time.time()
    GraphicThread.start()
    
def stop():
    '''
    stops the graphic thread
    '''
    running = False
    GraphicThread.join()
