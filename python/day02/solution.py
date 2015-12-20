import sys

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

area = 0
for line in sys.stdin.readlines():
    area = area + computeArea(line)
print area
