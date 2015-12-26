#! /usr/bin/env python

import sys
from optparse import OptionParser

def breakdown(line):
    if not line:
        return []

    output = []
    current = [line[0]]
    for c in line[1:]:
        if c == current[0]:
            current.append(c)
        else:
            output.append(current)
            current = [c]
    output.append(current)
    return output
        
################

def look_and_say(line):
    output = ''
    components = breakdown(line) 
    for component in components:
        output += str(len(component))
        output += component[0]
    return output

###################

parser = OptionParser()
parser.add_option('-c','--count', type='int', default='40')
(options, args) = parser.parse_args()

line = sys.stdin.readline().strip()
for i in xrange(options.count):
    line = look_and_say(line)
print len(line)
        
