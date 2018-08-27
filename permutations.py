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

def permutations_iterative(n):
    function_stack = []
    returning = False
    return_val = None
    function_stack.append((n, returning, return_val))
    while function_stack:
        (n, returning, return_val) = function_stack[-1]
        if returning == False:
            if len(n) < 1:
                returning = True
                return_val = [n]
                function_stack.pop()
                function_stack[-1] = (function_stack[-1][0],
                                      returning, return_val)
                continue
            function_stack.append((n[1:], False, None))
            continue
        else:
            root_perms = []
            for permutation in return_val:
                for i in range(len(permutation)+1):
                    root_perms.append(
                        permutation[0:i] + [n[0]] + permutation[i:]
                    )
            returning = True
            return_val = root_perms
            function_stack.pop()
            if function_stack:
                function_stack[-1] = (function_stack[-1][0],
                                      returning, return_val)
    return return_val

class FunctionStack():
    def __init__(self):
        self.stack_frames = []
        self.child_return_val = None
        self.child_just_returned = False

    def append(self, stack_frame):
        self.stack_frames.append(stack_frame)
        self.child_return_val = None
        self.child_just_returned = False

    def return_(self, return_val):
        self.stack_frames.pop()
        self.child_return_val = return_val
        self.child_just_returned = True

    def stack_frame_variables(self):
        return self.stack_frames[-1].variables

class StackFrame():
    def __init__(self, variables=None):
        self.variables = variables

def permutations_iterative2(n):
    function_stack = FunctionStack()
    function_stack.append(StackFrame(n))
    while len(function_stack.stack_frames) > 0:
        n = function_stack.stack_frame_variables()
        print(n)
        if function_stack.child_just_returned == False:
            if len(n) < 1:
                function_stack.return_([n])
                continue
            function_stack.append(StackFrame(n[1:]))
            continue
        else:
            root_perms = []
            for permutation in function_stack.child_return_val:
                for i in range(len(permutation)+1):
                    root_perms.append(
                        permutation[0:i] + [n[0]] + permutation[i:]
                    )
            function_stack.return_(root_perms)
    return function_stack.child_return_val

print(permutations_iterative2([1,2,3]))
