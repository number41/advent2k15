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

def count_line_second_half(line):
    actual = len(line)
    encoded = 2 # base two for the wrapping quotes
    cursor = 0
    while cursor < actual:
        if line[cursor] == '"':
            encoded += 2
        elif line[cursor] == '\\':
            encoded += 2
        else:
            encoded += 1 
        cursor += 1
    return (actual, encoded)

actual = 0
encoded = 0
for line in sys.stdin.readlines():
    (a, e) = count_line_second_half(line)
    actual += a
    encoded += e
print encoded - actual
