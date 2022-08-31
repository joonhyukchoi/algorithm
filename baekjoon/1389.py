import sys
from collections import deque

inp = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, inp().split())
graph = [[] for _ in range(n + 1)]

# for i in range(m):
#     a, b = map(int, inp().split())
#     if b not in graph[a]:
#         graph[a].append(b)
#     if a not in graph[b]:
#         graph[b].append(a)
# 플로이드와샬 풀이
INF = 10**9
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            distance[i][j] = 0
        
for i in range(m):
    a, b = map(int, inp().split())
    distance[a][b] = 1  
    distance[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

s = INF
index = n
for i in range(n, 0, -1):
    ns = sum(distance[i]) - INF
    if s >= ns:
        index = i
        s = ns
print(index)

# bfs 풀이
# distance = [-1] * (n + 1)
# def bfs(i):
#     q = deque([i])
#     distance[i] = 0
#     while q:
#         pos = q.popleft()
#         for el in graph[pos]:
#             if distance[el] == -1:
#                 q.append(el)
#                 distance[el] = distance[pos] + 1
# minval = 1000000
# val = n
# for i in range(n, 0, -1):
#     bfs(i)
#     s = sum(distance)
#     # print(minval, s)
#     if minval >= s:
#         val = i
#         minval = s
#     distance = [-1] * (n + 1)
# print(val)
    



