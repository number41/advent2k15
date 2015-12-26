#! /usr/bin/env python

def breakdown(line):
    if not line:
        return []

    output = []
    current = [line[0]]
    for c in line[1:]:
        if c == current[0]:
            current.append(c)
        else:
            output.append(current)
            current = [c]
    output.append(current)
    return output

###########

def increment(password):
    new_pw = list(password)
    for i in xrange(1, len(new_pw) + 1):
        if new_pw[-i] == 'z':
            new_pw[-i] = 'a'
            continue
        else:
            new_pw[-i] = chr(ord(new_pw[-i]) + 1)
            return ''.join(new_pw)
    raise Exception('overflow!?')

###########

def includes_increase(password):
    for cursor in xrange(0, len(password) - 2):
        a = ord(password[cursor])
        b = ord(password[cursor+1]) - 1
        c = ord(password[cursor+2]) - 2
        if a == b  and a == c:
            return True
    return False

###########

def no_forbidden_letters(password):
    for i in 'iol':
        if i in password:
            return False
    return True

###########

def two_different_pairs(password):
    # Get the occurrences of the same letter, and filter out the
    # cases where there's less than two
    components = filter(lambda c: len(c) >= 2, breakdown(password))

    # There needs to be at least two pairs
    if len(components) < 2:
        return False

    # But the pairs need to be different
    # The breakdown function takes care of any overlaps,
    # so just a set should be enough
    derp = { x[0] for x in components }
    return len(derp) >= 2 

###########

def next_pw(pw):
    checks = [two_different_pairs, no_forbidden_letters, includes_increase]
    while True:
        pw = increment(pw)
        if two_different_pairs(pw) and \
           no_forbidden_letters(pw) and \
           includes_increase(pw):
            return pw
        

###########

print next_pw('vzbxxyzz')
