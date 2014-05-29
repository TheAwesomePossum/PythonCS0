'''
Author: Graham C. Montgomery
Western State Colorado University

This file contains the project wide globals for the engine
'''

# External imports
import pygame

# Internal imports
from World import World


startTime = 0.0 # will hold the time in which the game was started
deltaTime = 0.02 # The time in seconds for the engine to go refresh the screen
refreshTime = 0.0 # the next time the screen will refresh
world = World() # is the list of objects to be rendered by the engine