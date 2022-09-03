import heapq
import sys

inp = sys.stdin.readline
v, e = map(int, inp().split())
graph = []
parent = [0] * (v + 1)
for i in range(0, v + 1):
    parent[i] = i
for i in range(e):
    a, b, t = map(int, inp().split())
    graph.append((t, a, b))
graph.sort()
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

s = 0
for el in graph:
    t, a, b = el
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        s += t
print(s)