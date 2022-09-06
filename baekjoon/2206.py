import sys
from collections import deque
import heapq
inp = sys.stdin.readline
n, m = map(int, inp().split())
graph = []
for i in range(n):
    graph.append(list(map(int, inp().rstrip())))
q = deque()
# q = []
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
def bfs():
    graph[0][0] = 2
    q.append((0, 0, 1, True))
    while q:
        x, y, dist, broken = q.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    if broken == False:
                        graph[nx][ny] = 2
                    else:
                        graph[nx][ny] = 3
                    q.append((nx, ny, dist + 1, broken))
                elif graph[nx][ny] == 1 and broken:
                    graph[nx][ny] = 3
                    q.append((nx, ny, dist + 1, False))
                elif graph[nx][ny] == 2 and broken:
                    graph[nx][ny] = 3
                    q.append((nx, ny, dist + 1, broken))
    return -1
        
print(bfs())