'''
Author: Graham Montgomery
Western State Colorado University

This file will handle all events
'''

import sys

import Globals as g
import Engine
import time

pygame = g.pygame

'''
QUIT             none
ACTIVEEVENT      gain, state
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
JOYAXISMOTION    joy, axis, value
JOYBALLMOTION    joy, ball, rel
JOYHATMOTION     joy, hat, value
JOYBUTTONUP      joy, button
JOYBUTTONDOWN    joy, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT    
'''
def eraseEvents():
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    pygame.event.set_blocked(pygame.KEYDOWN)
    pygame.event.set_blocked(pygame.KEYUP)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    #pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.JOYAXISMOTION)
    pygame.event.set_blocked(pygame.JOYBALLMOTION)
    pygame.event.set_blocked(pygame.JOYHATMOTION)
    pygame.event.set_blocked(pygame.JOYBUTTONUP)
    pygame.event.set_blocked(pygame.JOYBUTTONDOWN)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.VIDEOEXPOSE)
    pygame.event.set_blocked(pygame.USEREVENT)
    
#### Vars for mouse dragged
g.draggedEventActive = False
g.mouseDown = False


eraseEvents()
EventList = {}

def noHandle(evt):
    pass

def updateEvents():
    #print("here")
    for evt in pygame.event.get():
        if evt.type is pygame.QUIT:
            #Engine.stop()
            if g.multithreading:
                Engine.stop()
            pygame.quit()
            sys.exit()
        #print(pygame.event.event_name(evt.type))
        EventList[pygame.event.event_name(evt.type)](evt)
        if g.draggedEventActive:
            if evt.type is pygame.MOUSEBUTTONDOWN:
                g.mouseDown = True
            elif evt.type is pygame.MOUSEBUTTONUP:
                g.mouseDown = False
            #print(g.mouseDown)
            if g.mouseDown and (evt.type is pygame.MOUSEMOTION):
                EventList["MouseDragged"](evt) 
        
def addMouseClickedEvent(handle):
    #pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    EventList[pygame.event.event_name(pygame.MOUSEBUTTONDOWN)] = handle
    #print(EventList)
    
def addMouseReleasedEvent(handle):
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    EventList[pygame.event.event_name(pygame.MOUSEBUTTONUP)] = handle
    #print(EventList)
    
def addMouseMovedEvent(handle):
    pygame.event.set_allowed(pygame.MOUSEMOTION)
    EventList[pygame.event.event_name(pygame.MOUSEMOTION)] = handle
    #print(EventList)
    
def addKeyPressedEvent(handle):
    pygame.event.set_allowed(pygame.KEYDOWN)
    EventList[pygame.event.event_name(pygame.KEYDOWN)] = handle
    #print(EventList)
    
def addKeyReleasedEvent(handle):
    pygame.event.set_allowed(pygame.KEYUP)
    EventList[pygame.event.event_name(pygame.KEYUP)] = handle
    #print(EventList)
        
def addMouseDraggedEvent(handle):
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    pygame.event.set_allowed(pygame.MOUSEMOTION)
    if not ((pygame.event.event_name(pygame.MOUSEBUTTONDOWN) in EventList)):
        EventList[pygame.event.event_name(pygame.MOUSEBUTTONDOWN)] = noHandle
    if not ((pygame.event.event_name(pygame.MOUSEBUTTONUP) in EventList)):
        EventList[pygame.event.event_name(pygame.MOUSEBUTTONUP)] = noHandle
    if not ((pygame.event.event_name(pygame.MOUSEMOTION) in EventList)):
        EventList[pygame.event.event_name(pygame.MOUSEMOTION)] = noHandle
    g.draggedEventActive = True
    EventList["MouseDragged"] = handle
    
def waitForClick():
    cont = True
    while(cont):
        for evt in pygame.event.get():
            if evt.type is pygame.MOUSEBUTTONDOWN:
                cont = False