import sys
from collections import deque
inp = sys.stdin.readline
m, n, h = map(int, inp().split())
# graph = [[[0,1],[2,3],[4,5]],[[6,7],[8,9],[10,11]]]
# print(graph[0][1][0])
graph = [[] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, inp().split())))
# print(graph)
q = deque()
count = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k, 0))
            elif graph[i][j][k] == 0:
                count += 1
s = 0
max_dist = 0
while q:
    now_h, now_n, now_m, dist = q.popleft()
    max_dist = max(dist, max_dist)
    for i in range(6):
        next_h = now_h + dx[i]
        next_n = now_n + dy[i]
        next_m = now_m + dz[i]
        if 0 <= next_h < h and 0 <= next_n < n and 0 <= next_m < m and graph[next_h][next_n][next_m] == 0:
            graph[next_h][next_n][next_m] = 1
            q.append((next_h, next_n, next_m, dist + 1))
            s += 1
if s == count:
    print(max_dist)
else:
    print(-1)