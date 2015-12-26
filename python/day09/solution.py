#! /usr/bin/env python

import sys
from collections import defaultdict
import itertools

distances = defaultdict(dict)
cities = set()
for line in sys.stdin.readlines():
    tokens = [t.strip() for t in line.split(' ')]
    distances[tokens[0]][tokens[2]] = int(tokens[4])
    distances[tokens[2]][tokens[0]] = int(tokens[4])
    cities.add(tokens[0])
    cities.add(tokens[2])

shortest_dist = -1
shortest_route = []
for orderings in itertools.permutations(cities):
    total = 0
    for cursor in xrange(len(orderings) - 1):
        first = orderings[cursor]
        second = orderings[cursor + 1]
        total += distances[first][second]
    if total > shortest_dist:
        shortest_dist = total
        shortest_route = orderings

print "Longest route at %d is %s" % (shortest_dist, ' -> '.join(shortest_route))
        
