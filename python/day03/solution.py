#! /usr/bin/env python
import sys

unique_locations = set()

x = 0
y = 0
unique_locations.add((x,y))

for c in sys.stdin.readline():
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1

    unique_locations.add((x,y))

print len(unique_locations)
    
