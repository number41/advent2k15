#! /usr/bin/env python

import re
import sys

INSTRUCTION_REGEX = "(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"

def get_directions(line):
    m = re.match(INSTRUCTION_REGEX, line)
    if not m:
        raise Exception("invalid instruction")
    (instr, sx, sy, ex, ey) = m.groups()
    return (instr, int(sx), int(sy), int(ex), int(ey))

#######

DIMENSION = 1000
BOARD = [[False for x in xrange(DIMENSION)] for x in xrange(DIMENSION)]

def turnOn(val):
    return True

def turnOff(val):
    return

def toggle(val):
    return not val

def handleAction(board, sx, sy, ex, ey, func):
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            BOARD[x][y] = func(BOARD[x][y]) 

def countBoard(board):
    i = 0
    for row in board:
        for col in row:
            if col:
                i += 1
    return i

instr_map = {'turn on':turnOn, 'turn off':turnOff, 'toggle':toggle}
for line in sys.stdin.readlines():
    (instr, start_x, start_y, end_x, end_y) = get_directions(line)
    func = instr_map[instr]
    handleAction(BOARD, start_x, start_y, end_x, end_y, func)
print countBoard(BOARD)
