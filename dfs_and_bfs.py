#!/usr/bin/env python3.5

from collections import deque
from copy import deepcopy

"""
Adjacency List
No cycle detection
"""


def dfs1(G, s, t):
    print(s)
    if s == t:
        return True
    for u in G[s]:
        if dfs1(G, u, t):
            return True
    return False


def bfs1(G, s, t):
    q = deque()
    q.append(s)
    while q:
        k = q.popleft()
        print(k)
        if k == t:
            return True
        for u in G[k]:
            q.append(u)
    return False


"""
Adjacency List
cycle detection
"""


def dfs2(G, s, t, v):
    print(s)
    v.add(s)
    if s == t:
        return True
    for u in G[s]:
        if u in v:
            continue
        if dfs2(G, u, t, v):
            return True
    return False


def bfs2(G, s, t):
    v = set()
    q = deque()
    q.append(s)
    while q:
        k = q.popleft()
        v.add(k)
        print(k)
        if k == t:
            return True
        for u in G[k]:
            if u in v:
                continue
            q.append(u)
    return False


"""
Adjacency List with weights
cycle detection
"""


def dfs3(G, s, t, v):
    print(s)
    v.add(s)
    if s == t:
        return True
    for (u, d) in G[s]:
        if u in v:
            continue
        if dfs3(G, u, t, v):
            return True
    return False


def bfs3(G, s, t):
    v = set()
    q = deque()
    q.appendleft(s)
    while q:
        k = q.pop()
        v.add(k)
        print(k)
        if k == t:
            return True
        for (u, d) in G[k]:
            if u in v:
                continue
            q.appendleft(u)
    return False


"""
Adjacency Matrix with weights
cycle detection
"""


def dfs4(G, s, t, v):
    v.add(s)
    print(s)
    if s == t:
        return True
    for (i, u) in enumerate(G[s]):
        if u <= 0:
            continue
        if i in v:
            continue
        if dfs4(G, i, t, v):
            return True
    return False


def bfs4(G, s, t):
    v = set()
    q = deque()
    q.appendleft(s)
    while q:
        k = q.pop()
        v.add(k)
        print(k)
        if k == t:
            return True
        for (i, u) in enumerate(G[k]):
            if u <= 0:
                continue
            if i in v:
                continue
            q.appendleft(i)
    return False


"""
Other implementations
"""


def dfs5(G, s, t):
    """
    Args:
        G (dict): A hashmap of adjacency lists of the graph G
        s: Starting node
        t: Target node
    Returns:
        path (list): A path from s to t.
                     path==[] if there is no such path
    """

    def dfs5_helper(G, u, t, visited):
        """
        Args:
            u: Current node
            visited (set): A hashset of nodes already visited
        Returns:
            path (list): A path from u to t.
                         path==[] if there is no such path
        """
        path = []
        visited.add(u)
        path.append(u)
        if u == t:
            return path
        for neighbour in G[u]:
            if neighbour in visited:
                continue
            path_left = dfs5_helper(G, neighbour, t, visited)
            if path_left != []:
                return path + path_left
        return []

    return dfs5_helper(G, s, t, set())


def dfs5_iterative(G, s, t):
    """
    Args:
        G (dict): A hashmap of adjacency lists of the graph G
        s: Starting node
        t: Target node
    Returns:
        path (list): A path from s to t.
                     path==[] if there is no such path
    """
    visited = set()
    path = list()

    stack = []
    fifo = deque()  # first in first out
    fifo.appendleft((G, s, t, visited))
    stack.append(fifo)
    return_queue = deque()  # first in first out
    while len(stack) > 0:
        fifo = stack.pop()
        (G, u, t, visited) = fifo.pop()
        if len(fifo) > 0:
            stack.append(fifo)
        new_fifo = deque()

        if len(return_queue) > 0 and return_queue[0] != []:
            return_queue.appendleft([u])
            continue

        path = []
        visited.add(u)
        path.append(u)
        if u == t:
            return_queue.appendleft(path)
            continue
        for neighbour in G[u]:
            if neighbour in visited:
                continue
            new_fifo.appendleft((G, neighbour, t, visited))
        if len(new_fifo) > 0:
            stack.append(new_fifo)
            continue
        return_queue.appendleft([])

    return_val = []
    while len(return_queue) > 0:
        return_val += return_queue.pop()
    return return_val


graph1 = dict()
graph1[1] = [2, 3, 4]
graph1[2] = [5, 6]
graph1[3] = [7, 8]
graph1[4] = [9, 10]
graph1[5] = []
graph1[6] = []
graph1[7] = []
graph1[8] = []
graph1[9] = []
graph1[10] = []

graph1_with_cycle = deepcopy(graph1)
graph1_with_cycle[5] = [6]
graph1_with_cycle[6] = [5]

print("dfs1")
dfs1(graph1, 1, 8)

# would throw RecursionError:
# dfs1(graph1_with_cycle, 1, 8)

print("bfs1")
bfs1(graph1, 1, 8)

print("bfs1")
# Might be checking the same nodes many times for some graphs
bfs1(graph1_with_cycle, 1, 8)

print("dfs2")
dfs2(graph1, 1, 8, set())

print("dfs2")
dfs2(graph1_with_cycle, 1, 8, set())

print("bfs2")
bfs2(graph1, 1, 8)

print("bfs2")
bfs2(graph1_with_cycle, 1, 8)

graph2 = dict()
graph2[1] = [(2, 3), (3, 3), (4, 3)]
graph2[2] = [(5, 2), (6, 3)]
graph2[3] = [(7, 5), (8, 2)]
graph2[4] = [(9, 15), (10, 20)]
graph2[5] = []
graph2[6] = []
graph2[7] = []
graph2[8] = []
graph2[9] = []
graph2[10] = []

graph2_with_cycle = deepcopy(graph2)
graph2_with_cycle[5] = [(6, 100)]
graph2_with_cycle[6] = [(5, 100)]

print("dfs3")
dfs3(graph2, 1, 8, set())
print("dfs3")
dfs3(graph2_with_cycle, 1, 8, set())
print("bfs3")
bfs3(graph2, 1, 8)
print("bfs3")
bfs3(graph2_with_cycle, 1, 8)

graph3 = [
    [0, 3, 3, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 15, 20],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

graph3_with_cycle = [
    [0, 3, 3, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 15, 20],
    [0, 0, 0, 0, 0, 100, 0, 0, 0, 0],
    [0, 0, 0, 0, 100, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print("dfs4")
dfs4(graph3, 0, 7, set())
print("dfs4")
dfs4(graph3_with_cycle, 0, 7, set())
print("bfs4")
bfs4(graph3, 0, 7)
print("bfs4")
bfs4(graph3_with_cycle, 0, 7)

print("dfs5")
print(dfs5(graph1_with_cycle, 1, 8))
print("dfs5_iterative")
print(dfs5_iterative(graph1_with_cycle, 1, 8))
