#!/usr/bin/env python3.5

from math import inf

class Node():
    def __init__(self, name, covered):
        self.name = name
        self.covered = covered
        self.previous = None

def dijkstra(G, s, t):
    visited = set()
    nodes = dict()
    for u in G:
        nodes[u] = Node(u, inf)
    nodes[s].covered = 0
    shortest_path = dict()

    while len(visited) < len(G):
        current = nodes.pop_least_covered()
        visited.add(current.name)
        for (u, dist) in G[k]:
            if u in visited:
                continue
            if current.covered + dist < nodes[u].covered:
                nodes[u].covered = current.covered + dist
                nodes[u].previous = current.name
    return nodes[t].covered

G = dict()
G[1] = [(2, 5),(3, 6),(4, 2)]
G[2] = [(6, 3), (3, 1)]
G[3] = [(5, 5), (6, 1), (7, 15)]
G[4] = [(5, 7)]
G[5] = [(7, 4)]
G[6] = [(2, 2), (7, 3)]
