#! /usr/bin/env python
import itertools
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
robot = Entity()
unique_locations.add(santa.coords)
unique_locations.add(robot.coords)

for (c,entity) in zip(sys.stdin.readline(), itertools.cycle([santa,robot])):
    if c == '<':
        entity.dec_x()
    elif c == '>':
        entity.inc_x()
    elif c == '^':
        entity.inc_y()
    elif c == 'v':
        entity.dec_y()

    unique_locations.add(entity.coords)

print len(unique_locations)
    
