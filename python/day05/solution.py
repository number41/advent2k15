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

#################

def twicePair(text):
    i = 0
    while i < len(text) - 2:
        start = i + 2
        pair = text[i:start]
        if pair in text[start:]:
            return True
        i += 1
    return False

def repeatCheck(text):
    i = 0
    while i < len(text) - 2:
        if text[i] == text[i+2]:
            return True
        i += 1
    return False

def checkLine_SecondHalf(text):
    for check in [twicePair, repeatCheck]:
        if not check(text):
            return False
    return True

#######

print len(filter(lambda l: checkLine_SecondHalf(l), sys.stdin.readlines()))    
