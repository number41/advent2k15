#! /usr/bin/env python
import sys

unique_locations = set()

class Entity(object):
    def __init__(self):
       self._x = 0
       self._y = 0

    @property
    def coords(self):
        return (self._x, self._y)

    def inc_x(self):
        self._x += 1
    def dec_x(self):
        self._x -= 1
    def inc_y(self):
        self._y += 1
    def dec_y(self):
        self._y -= 1

############################
 
santa = Entity()
unique_locations.add(santa.coords)

for c in sys.stdin.readline():
    if c == '<':
        santa.dec_x()
    elif c == '>':
        santa.inc_x()
    elif c == '^':
        santa.inc_y()
    elif c == 'v':
        santa.dec_y()

    unique_locations.add(santa.coords)

print len(unique_locations)
    
