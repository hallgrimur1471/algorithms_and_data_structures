#!/usr/bin/env python3.5

#Text space:
#
#
#
#Code space:

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def paths_with_sum(T, S):
    current_sum = 0
    sum_hashmap = dict()
    _paths_with_sum_helper(T, S, current_sum, sum_hashmap)

def _paths_with_sum_helper(T, S, current_sum, sum_hashmap):
    if T == None:
        return 0
    current_sum += T.value
    if (S - current_sum) in sum_hashmap:
        num_paths_from_current = sum_hashmap[S - current_sum]

    if current_sum in sum_hashmap:
        sum_hashmap[current_sum] += 1
    else:
        sum_hashmap[current_sum] = 1

    num_paths_in_left = 0
    num_paths_in_right = 0
    if T.left != None:
        num_paths_in_left += (
            _paths_with_sum_helper(T.left, S, current_sum, sum_hashmap)
        )
    if T.right != None:
        num_paths_in_right += (
            _paths_with_sum_helper(T, S, current_sum, sum_hashmap)
        )

    sum_hashmap[current_sum] -= 1

    return num_paths_from_current + num_paths_in_left + num_paths_in_right


# first implementation

def paths_with_sum(T, S):
    complements = set()
    _paths_with_sum_helper(T, S, complements)

def _paths_with_sum_helper(T, S, complements):
    path_count = 0
    if T.value in complements:
        path_count += 1
    for c in complements:
        complements[c] -= T.value
    complements.add(S - T.value)
    path_count_left = _paths_with_sum_helper(T.left, S, complements)
    path_count_right = _paths_with_sum_helper(T.right, S, complements)

    return path_count + path_count_left + path_count_right

