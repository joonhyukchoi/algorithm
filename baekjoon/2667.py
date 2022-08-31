import sys
inp = sys.stdin.readline
n = int(inp())
apart = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = inp().strip()
    apart[i].append(0)
    for el in temp:
        apart[i].append(int(el))
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def dfs(x, y): 
    count = 0
    apart[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= n and apart[nx][ny] != 0:
            count += dfs(nx, ny)
    return count + 1

counts = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if apart[i][j] != 0:
            counts.append(dfs(i, j))
print(len(counts))
counts.sort()
for el in counts:
    print(el)
