# pypy로 돌려야 시간초과 안뜸
import sys
import heapq
inp = sys.stdin.readline

n, m, x = map(int, inp().split())
INF = 10**9
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, t = map(int, inp().split())
    graph[a].append([b, t])


dist_x = [INF] * (n + 1) 
heap_x = []
dist_x[x] = 0
heapq.heappush(heap_x, (x, 0))
while heap_x:
    now, now_d = heapq.heappop(heap_x)
    if dist_x[now] < now_d:
        continue
    for el in graph[now]:
        new = el[1] + now_d
        if dist_x[el[0]] > new:
            dist_x[el[0]] = new
            heapq.heappush(heap_x, (el[0], new))
ans = 0
for i in range(1, n + 1):
    dist = [INF] * (n + 1) 
    heap = []
    dist[i] = 0
    heapq.heappush(heap, (i, 0))
    while heap:
        now, now_d = heapq.heappop(heap)
        if dist[now] < now_d:
            continue
        for el in graph[now]:
            new = el[1] + now_d
            if dist[el[0]] > new:
                dist[el[0]] = new
                heapq.heappush(heap, (el[0], new))
    if ans < dist[x] + dist_x[i]:
        ans = dist[x] + dist_x[i]
print(ans)
    

# 플로이드 와샬 풀이 시간초과
# import sys
# inp = sys.stdin.readline

# n, m, x = map(int, inp().split())
# INF = 10**9
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     a, b, t = map(int, inp().split())
#     graph[a][b] = t

# for k in range(n + 1):
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if i != j:
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# max_num = 0
# for i in range(1, n + 1):
#     now = graph[i][x] + graph[x][i]
#     if max_num < now and i != x:
#         max_num = now
# print(max_num)

