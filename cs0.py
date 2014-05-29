'''
Author: Graham Montgomery
Western State Colorado University

This file is the baisic import file for any cs0 project. It will hold some baisic functions for manipulating the world and starting the engine
'''

import time

import Globals
import Engine

from Colors import *

WindowWidth = 500
WindowHeight = 500
WindowCaption = "Game Window"
WindowColor = WHITE

def add(obj):
    Globals.world.add(obj)

def start():
    Engine.start(WindowWidth, WindowHeight, WindowCaption, WindowColor)

def stop():
    Engine.stop()
    
def pause(t):
    time.sleep(t)