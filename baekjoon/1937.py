import sys
inp = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(inp())
graph = [[-1] * n for _ in range(n)]
mp = []
for i in range(n):
    mp.append(list(map(int,inp().split())))

def dfs(x, y):
    if graph[x][y] != -1:
        return graph[x][y]
    maxtemp = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n and mp[x][y] < mp[nx][ny]:
            maxtemp = max(maxtemp, dfs(nx, ny))
    graph[x][y] = 1 + maxtemp
    return 1 + maxtemp
maxval = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == -1:
            dfs(i, j)
            maxval = max(graph[i][j], maxval)
print(maxval)
