import sys
from collections import defaultdict
from collections import deque

inp = sys.stdin.readline

N, M, K, X = map(int, inp().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, inp().split())
    graph[a].append(b)

dist = [-1] * (N + 1)
dist[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if dist[next_node] == -1:
            dist[next_node] = dist[now] + 1
            q.append(next_node)

check = False
for i in range(1, N + 1):
    if dist[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)