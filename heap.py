#!/usr/bin/env python3.5

class Heap():
    def __init__(self):
        self._nodes = []

    def insert(self, value):
        self._nodes.append(value)
        self._fix_up()

    def pop(self):
        value = self._nodes[0]
        self._nodes[0] = self._nodes[-1]
        self._nodes.pop()
        self._fix_down()
        return value

    def is_empty(self):
        return len(self._nodes) == 0

    def _fix_up(self):
        x = len(self._nodes) - 1
        p = self._get_parent(x)
        while (p >= 0) and (self._nodes[x] < self._nodes[p]):
            self._swap(p, x)
            x = p
            p = self._get_parent(x)

    def _fix_down(self):
        x = 0
        l = self._get_left_child(x)
        r = self._get_right_child(x)
        while (
            (
                (l < len(self._nodes)) and
                (r < len(self._nodes))
            ) and
            (
                (self._nodes[x] > self._nodes[l]) or
                (self._nodes[x] > self._nodes[r])
            )
        ):
            if self._nodes[l] < self._nodes[r]:
                self._swap(x, l)
                x = l
            else:
                self._swap(x, r)
                x = r
            l = self._get_left_child(x)
            r = self._get_right_child(x)
        if (
            (l < len(self._nodes)) and
            (r >= len(self._nodes)) and
            (self._nodes[x] > self._nodes[l])
        ):
            self._swap(x, l)

    def _swap(self, i, j):
        tmp = self._nodes[i]
        self._nodes[i] = self._nodes[j]
        self._nodes[j] = tmp

    def _get_parent(self, x):
        if x % 2 == 0: # x is right child
            return (x // 2) - 1
        else: # x is left child
            return (x - 1) // 2

    def _get_left_child(self, i):
        return 2*i + 1

    def _get_right_child(self, i):
        return 2*i + 2

from random import randint
from time import time
r = []
for _ in range(400000):
    r.append(randint(0, 888888888))
start = time()
h = Heap()
for _ in range(200000):
    h.insert(r.pop())
    print(h.pop())
    h.insert(r.pop())
while h.is_empty() == False:
    value = h.pop()
    print(value, "####")
print(time() - start, "seconds")
print("888888888")
