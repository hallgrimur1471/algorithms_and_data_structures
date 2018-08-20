#!/usr/bin/env python3.5

"""
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create
an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
subtree of n is identical to T2. That is, if you cut off the tree at node n,
the two trees would be identical. 
"""

from copy import deepcopy

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_post_order(t1, t2):
    found = traverse_post_order(t1.left, t2)
    if found == False:
        found = traverse_post_order(t1.right, t2)
    if found == False:
        found = is_equal(t1, t2)
    return found

def is_equal(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None and t2 != None:
        return False
    if t1 != None and t2 == None:
        return False
    return (
        t1.value == t2.value and
        is_equal(t1.left, t2.left) and
        is_equal(t1.right == t2.right)
    )

if __name__ == "__main__":
    t2 = Node(8)
    t2.left = Node(2)
    t2.right = Node(10)

    t1 = Node(6)
    t1.right = deepcopy(t2)
    t1.left = Node(4, left=Node(3, left=Node(1), right=Node(5)), right=Node(12))

    traverse_post_order(t1, t2)
