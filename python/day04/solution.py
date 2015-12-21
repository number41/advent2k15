#! /usr/bin/env python
import sys
import md5
from optparse import OptionParser

###################

def find_number(key,zeroes=5):
    prefix = '0' * zeroes
    i = 0
    while True:
        i += 1
        val = md5.md5('%s%d' % (key, i)).hexdigest()
        if val.startswith(prefix):
            return i

###################

parser = OptionParser()
parser.add_option('-z','--zeroes', default='5', type='int')
(options,args) = parser.parse_args()

print find_number(sys.stdin.readline().strip(), options.zeroes)
