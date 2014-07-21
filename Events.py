'''
Author: Graham Montgomery
Western State Colorado University

This file will handle all events
'''

import sys

import Globals as g
import Engine

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
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.JOYAXISMOTION)
    pygame.event.set_blocked(pygame.JOYBALLMOTION)
    pygame.event.set_blocked(pygame.JOYHATMOTION)
    pygame.event.set_blocked(pygame.JOYBUTTONUP)
    pygame.event.set_blocked(pygame.JOYBUTTONDOWN)
    pygame.event.set_blocked(pygame.VIDEORESIZE)
    pygame.event.set_blocked(pygame.VIDEOEXPOSE)
    pygame.event.set_blocked(pygame.USEREVENT)


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
        
def addMouseClickedEvent(handle):
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    EventList[pygame.event.event_name(pygame.MOUSEBUTTONDOWN)] = handle
    print(EventList)
        