#!/usr/bin/env python3.5

from collections.abc import Sequence

def rotate_right(s, c):
    """
    Args:
        s (collections.abc.Sequence): Sequence to be rotated. Python strings and
        lists are examples of a Python Sequence.
        c (int): Specifies how many places the elements of s should be rotated.
    Returns:
        s (collections.abc.Sequence): All elements of s have been moved c places
        foward. s is assumed to be "circular" so an element that was previously 
        at index i is now at index (i+c)%len(s)
    """
    if not isinstance(s, Sequence):
        TypeError("s must inherit from collections.abc.Sequence")
    if not isinstance(c, int):
        TypeError("c must be an int")
    if c < 0:
        ValueError("c must be positive")
    N = len(s)
    if N == 0:
        return s
    new_start = (N-c)%N
    new_s = s[new_start:] + s[:new_start]
    return new_s

# tests
assert rotate_right("abcdef", 2) == "efabcd"
assert rotate_right("abc", 3) == "abc"
assert rotate_right("abc", 4) == "cab"
assert rotate_right([1,2,3], 0) == [1,2,3]
assert rotate_right([1,2,3], 1) == [3,1,2]
assert rotate_right("", 20) == ""
assert rotate_right([], 0) == []

def permutations(n):
    if len(n) <= 1:
        return [n]
    root_perms = []
    for permutation in permutations(n[1:]):
        for i in range(len(permutation)+1):
            root_perms.append(permutation[0:i] + [n[0]] + permutation[i:])
    return root_perms

#for p in permutations([1,2,3]):
#    print(p)
#print(rotate_right("abcdef", 2))
