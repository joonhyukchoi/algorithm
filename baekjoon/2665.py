from re import A
import sys
import heapq
inp = sys.stdin.readline
n = int(inp())
graph = []
for _ in range(n):
    graph.append(list(map(int, inp().rstrip())))
flag = [[True] * (n + 1) for _ in range(n + 1)]
heap = []
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
heapq.heappush(heap, (0, 1, 1))
while heap:
    dist, x, y = heapq.heappop(heap)
    if x == n and y == n:
        print(dist)
    flag[x][y] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= n and flag[nx][ny] == True:
            flag[nx][ny] = False
            if graph[nx - 1][ny - 1] == 1:
                heapq.heappush(heap, (dist, nx, ny))
            else:
                heapq.heappush(heap, (dist + 1, nx, ny))