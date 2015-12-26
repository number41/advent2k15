#! /usr/bin/env python

import sys
import json

def sum_list(data):
    sum = 0
    for datum in data:
        sum += sum_data(datum)
    return sum

#########################

def sum_dict(data):
    if 'red' in data.itervalues():
        return 0

    sum = 0
    for datum in data.itervalues():
        sum += sum_data(datum)
    return sum

#########################

def sum_data(data):
    if isinstance(data, list):
        return sum_list(data)
    elif isinstance(data, dict):
        return sum_dict(data)
    elif isinstance(data, int):
        return data

    return 0

#########################

print sum_data(json.loads(sys.stdin.readline()))

