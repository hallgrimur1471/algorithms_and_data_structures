#!/usr/bin/env python3.5

def permutations(n):
    if len(n) <= 1:
        return [n]
    root_perms = []
    for permutation in permutations(n[1:]):
        for i in range(len(permutation)+1):
            root_perms.append(permutation[0:i] + [n[0]] + permutation[i:])
    return root_perms

for p in permutations([1,2,3]):
    print(p)
