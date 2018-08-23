#!/usr/bin/env python3.5

def rob(n):
    a = 0
    b = n[0]
    for i in range(1, len(n)):
        c = max(n[i] + a, b)
        a = b
        b = c
    return c

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
