'''
Author: Graham Montgomery
Western State Colorado University

This constructs the concurency safe world list
'''

import threading

class World:
    
    def __init__(self):
        self._lock = threading.Lock()
        self.world = []
        
    def acquire(self):
        self._lock.acquire()
    def release(self):
        self._lock.release()
        
    def add(self, obj):
        self.world.append(obj)
        
    def remove(self, obj):
        self.world.remove(obj)