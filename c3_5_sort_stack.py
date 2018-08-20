#!/usr/bin/env python3.5

"""
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty. 
"""

def sort_stack(s):
    r = []
    while len(s) > 0:
        v = s.pop()
        c = 0
        while r != [] and v > r[-1]:
            x = r.pop()
            s.append(x)
            c += 1
        r.append(v)
        for _ in range(0, c):
            x = s.pop()
            r.append(x)
    while len(r) > 0:
        x = r.pop()
        s.append(x)
    return s

if __name__ == "__main__":
    s = [46,6,8,3,6,7]
    sort_stack(s)
    print(s)
