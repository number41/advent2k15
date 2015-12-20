import sys

count = 0
for c in sys.argv[1]:
    if c == '(':
        count = count + 1
    elif c == ')':
        count = count - 1
print count
