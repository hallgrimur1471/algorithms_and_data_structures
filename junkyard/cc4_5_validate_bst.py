#!/usr/bin/env python3.5

"""
Implement a function to check if a binary tree is a binary search tree.
"""

from math import inf

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(|V|)
def is_binary_search_tree(t, mx, mn):
    if t == None:
        return (True, None, None)
    (is_bst, mx_left, mn_left) = is_binary_search_tree(t.left, mx, mn)
    if is_bst == False:
        return (False, None, None)
    (is_bst, mx_right, mn_right) = is_binary_search_tree(t.right, mx, mn)
    if is_bst == False:
        return (False, None, None)

    # is binary search tree check
    if t.left == None and t.right == None:
        return (True, t.value, t.value)
    if mx_left <= t.value and t.value < mn_right:
        return (True, mx_right, mn_left)
    return (False, None, None)

if __name__ == "__main__":
    t = Node(5,
        left = Node(3,
            left = Node(2,
                left = Node(1),
                right = Node(3),
            ),
            right = Node(4,
                left = Node(1),
                right = Node(5),
            ),
        ),
        right = Node(7),
    )
    print(is_binary_search_tree(t, -inf, inf))
    
    t = Node(5,
        left = Node(3,
            left = Node(2,
                left = Node(1),
                right = Node(3),
            ),
            right = Node(4,
                left = Node(4),
                right = Node(5),
            ),
        ),
        right = Node(7),
    )
    print(is_binary_search_tree(t, -inf, inf))

    t = None
    print(is_binary_search_tree(t, -inf, inf))

    t = Node(8)
    print(is_binary_search_tree(t, -inf, inf))
