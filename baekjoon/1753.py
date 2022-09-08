import heapq
import sys
inp = sys.stdin.readline
v, e = map(int, inp().split())
start = int(inp())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, w = map(int, inp().split())
    graph[a].append((b, w))
INF = 10**9
dist = [INF] * (v + 1)
heap = []
dist[start] = 0
heapq.heappush(heap, (0, start))
while heap:
    w, now = heapq.heappop(heap)
    if w > dist[now]:
        continue
    for el in graph[now]:
        nd = w + el[1]
        if dist[el[0]] > nd:
            dist[el[0]] = nd
            heapq.heappush(heap, (nd, el[0]))
dist.pop(0)
for i in dist:
    if i == INF:
        print('INF')
    else:
        print(i)