#!/usr/bin/env python3.5

from collections import deque
from math import inf

# using adjacency matrix
def max_flow(G, s, t):
    F = []
    N = len(G)
    for _ in range(0, N):
        F.append([0]*N)

    while True:
        # find valid path
        q = deque()
        q.appendleft((s, []))
        found = False
        while len(q) > 0:
            (i, path) = q.pop()
            if i == t:
                found = True
                path.append(i)
                break
            for j in range(0, N):
                if j in path:
                    continue
                if (
                    (0 <= F[i][j] and F[i][j] < G[i][j]) or
                    (F[i][j] < 0)
                ):
                    q.appendleft((j, path + [i]))


        if found == False:
            return sum(F[s])

        # augment path
        max_increase = inf
        for r in range(0, len(path)-1):
            u = path[r]
            v = path[r+1]
            if F[i][j] < 0:
                max_increase = min(max_increase, abs(F[u][v]))
            else:
                max_increase = min(max_increase, G[u][v] - F[u][v])
        
        for r in range(0, len(path)-1):
            u = path[r]
            v = path[r+1]
            F[u][v] += max_increase
            F[v][u] -= max_increase

G = [
    [0,3,3,4,0,0,0],
    [0,0,0,0,2,0,0],
    [0,10,0,0,1,0,0],
    [0,0,0,0,0,5,0],
    [0,0,0,0,0,1,2],
    [0,0,0,0,0,0,5],
    [0,0,0,0,0,0,0],
]
print(max_flow(G, 0, 6))
