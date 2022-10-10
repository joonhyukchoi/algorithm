import sys
import copy
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
n = int(inp())
graph = [[] for _ in range(n)]
for i in range(n):
    line = inp().rstrip()
    for j in range(n):
        graph[i].append(line[j])
graph2 = copy.deepcopy(graph)
count = 0
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def dfs(x, y, graph, bef):
    graph[x][y] = 'X'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'X' and graph[nx][ny] == bef:
            dfs(nx, ny, graph, bef)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 'X':
            dfs(i, j, graph, graph[i][j])
            count += 1
print(count)
count = 0
for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if graph2[i][j] != 'X':
            dfs(i, j, graph2, graph2[i][j])
            count += 1
print(count)