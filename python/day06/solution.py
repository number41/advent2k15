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
BOARD = [[0 for x in xrange(DIMENSION)] for x in xrange(DIMENSION)]

def turnOn(val):
    return val + 1

def turnOff(val):
    if val == 0:
        return 0
    else:
        return val - 1

def toggle(val):
    return val + 2

def handleAction(board, sx, sy, ex, ey, func):
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            BOARD[x][y] = func(BOARD[x][y]) 

def countBoard(board):
    return reduce(lambda row_acc, row: row_acc + reduce(lambda col_acc, col: col_acc + col, row, 0), board, 0)

instr_map = {'turn on':turnOn, 'turn off':turnOff, 'toggle':toggle}
for line in sys.stdin.readlines():
    (instr, start_x, start_y, end_x, end_y) = get_directions(line)
    func = instr_map[instr]
    handleAction(BOARD, start_x, start_y, end_x, end_y, func)
print countBoard(BOARD)
