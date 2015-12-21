import sys
from optparse import OptionParser

#################

def computeArea(token):
    tokens = token.split('x')
    length = int(tokens[0])
    width = int(tokens[1])
    height = int(tokens[2])

    lh = length*height
    lw = length*width
    wh = width*height
    
    area = 2*lh + 2*lw + 2*wh
    
    extra = lw
    if wh < extra:
        extra = wh
    if lh < extra:
        extra = lh
    
    return area + extra

#################

def computeRibbon(token):
    tokens = token.split('x')
    length = int(tokens[0])
    width = int(tokens[1])
    height = int(tokens[2])

    (a,b) = sorted([length, width, height])[0:2]
    base = 2*a + 2*b
    extra = length * width * height
       
    return extra+base

#################

parser = OptionParser()
parser.add_option("-r","--ribbon", action='store_true')
(options, args) = parser.parse_args()

if not options.ribbon:
    func = computeArea
else:
    func = computeRibbon

area = 0
for line in sys.stdin.readlines():
    area = area + func(line)
print area
