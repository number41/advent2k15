#! /usr/bin/env python

import sys

def vowelCheck(text):
    return len(filter(lambda c: c in 'aeiou', text)) >= 3

def twiceCheck(text):
    chars = set(text)
    for c in chars:
        if 2*c in text:
            return True

def naughtyList(text):
    for n in ['ab','cd','pq','xy']:
        if n in text:
            return False
    return True 

def checkLine_FirstHalf(text):
    for check in [vowelCheck, twiceCheck, naughtyList]:
        if not check(text):
            return False
    return True

#######

print len(filter(lambda l: checkLine_FirstHalf(l), sys.stdin.readlines()))    
