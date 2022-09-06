from queue import Empty
import sys
from collections import deque
inp = sys.stdin.readline
r, c = map(int, inp().split())
graph = [[] for _ in range(r)]
for i in range(r):
    temp = inp().rstrip()
    for el in temp:
        graph[i].append(el)
# print(graph)
start = ()
end = ()
q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append(('*', i, j, 0))
        elif graph[i][j] == 'D':
            end = (i, j)
        elif graph[i][j] == 'S':
            start = (i, j)
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
q.append(('S', start[0], start[1], 0))
ans = 0
while q:
    turn, x, y, dist = q.popleft()
    # print(graph, q)
    if x == end[0] and y == end[1] and turn == 'S':
        ans = dist
        break
    if turn == '*':
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                q.append(('*', nx, ny, dist + 1))
    else:
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == '.' or graph[nx][ny] == 'D'):
                graph[nx][ny] = 'S'
                q.append(('S', nx, ny, dist + 1))
if ans:
    print(ans)
else:
    print('KAKTUS')