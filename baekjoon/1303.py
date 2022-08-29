import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())
graph = []
flag = [[False for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(m):
    graph.append(inp().rstrip())
# print(flag)
def dfs(x, y, color):
    global count
    count += 1
    flag[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and flag[nx][ny] == False and color == graph[nx][ny]:
            dfs(nx, ny, color)

teamW = 0
teamB = 0
for i in range(m):
    for j in range(n):
        if flag[i][j] == False:
            count = 0
            color = graph[i][j]
            dfs(i, j, color)
            if color == 'W':
                teamW += count**2
            else:
                teamB += count**2
            count = 0
print(teamW, teamB)
