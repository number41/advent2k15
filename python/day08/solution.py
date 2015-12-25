#! /usr/bin/env python

import sys

def count_line(line):
    actual = len(line)
    inmem = 0
    cursor = 0
    while cursor < actual:
        if line[cursor] == '"':
            cursor += 1
            continue
        elif line[cursor] == '\\':
            if line[cursor+1] == 'x':
                cursor += 4
            else:
                cursor += 2
            inmem += 1
            continue
        else:
            cursor += 1
            inmem += 1 
    return (actual, inmem)

actual = 0
inmem = 0
for line in sys.stdin.readlines():
    (a, i) = count_line(line)
    actual += a
    inmem += i 
print actual - inmem
