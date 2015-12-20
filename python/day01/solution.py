import sys

count = 0
position = 0
for c in sys.argv[1]:
    position = position + 1

    if c == '(':
        count = count + 1
    elif c == ')':
        count = count - 1

    if count == -1:
        break

print position
