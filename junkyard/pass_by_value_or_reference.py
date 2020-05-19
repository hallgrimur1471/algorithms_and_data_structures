#!/usr/bin/env python3.5

from collections import deque

def mutate(int_, float_, str_, list1_, list2_, dict_, set_, deque_):
    int_ += 1000
    float_ += 1000.0
    str_ += " changed!"
    list1_.append(1000)
    list2_.append([1000])
    dict_[1] += 1000
    set_.add(1000)
    deque_.appendleft(1000)

i = 2
f = 2.0
str_ = "original"
l1 = [2]
l2 = [[2]]
d = {1: 2}
s = set()
s.add(2)
q = deque()
q.append(2)

mutate(i, f, str_, l1, l2, d, s, q)

for v in [i, f, str_, l1, l2, d, s, q]:
    print(v)
