#!/usr/bin/env python3.5

def min_flips(a, b):
    x = a ^ b
    c = 0
    for i in range(0, max(a.bit_length(), b.bit_length())):
        if ((1 << i) & x) != 0:
            c += 1
    return c

a = int('01111', 2)
b = int('01111', 2)
print(min_flips(a, b))
