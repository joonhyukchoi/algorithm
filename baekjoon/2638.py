import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
r, c = map(int, inp().split())
graph = []
for i in range(r):
    row = list(map(int, inp().split()))
    graph.append(row)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def sweep(graph, x, y, n):
    graph[x][y] = n - 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and n <= graph[nx][ny] <= 0:
            sweep(graph, nx, ny, n)

def check_all_removed():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                return False
    return True

def check_melt(graph, x, y, n):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] <= n - 1:
            count += 1
        if count >= 2:
            graph[x][y] = n
            break
cnt = 0 
while True:
    sweep(graph, 0, 0, -cnt)
    # print(graph)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                check_melt(graph, i, j, -cnt)
    # print(graph)
    if check_all_removed():
        break
    else:
        cnt += 1
print(cnt + 1)