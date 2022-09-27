import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
m, n = map(int, inp().split())
graph = []
for i in range(m):
    graph.append(list(map(int, inp().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, target, change):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == target:
            graph[nx][ny] = change
            dfs(nx, ny, target, change)

def remove():
    dfs(0, 0, 0, -1)

def melt():
    count = 0
    # 오른쪽방향 sweep
    for i in range(m):
        flag = 0
        for j in range(n):
            if graph[i][j] == -1:
                flag = 1
            elif graph[i][j] == 1:
                if flag == 1:
                    graph[i][j] = -100
                    count += 1
                flag = 0
            else:
                flag = -1
    # 왼쪽방향 sweep
    for i in range(m):
        flag = 0
        for j in reversed(range(n)):
            if graph[i][j] == -1:
                flag = 1
            elif graph[i][j] == 1:
                if flag == 1:
                    graph[i][j] = -100
                    count += 1
                flag = 0
            else:
                flag = -1
    # 아래방향 sweep
    for j in range(n):
        flag = 0
        for i in range(m):
            if graph[i][j] == -1:
                flag = 1
            elif graph[i][j] == 1:
                if flag == 1:
                    graph[i][j] = -100
                    count += 1
                flag = 0
            else:
                flag = -1
    # 위방향 sweep
    for j in range(n):
        flag = 0
        for i in reversed(range(m)):
            if graph[i][j] == -1:
                flag = 1
            elif graph[i][j] == 1:
                if flag == 1:
                    graph[i][j] = -100
                    count += 1
                flag = 0
            else:
                flag = -1
    # print(graph)
    for i in range(m):
        for j in range(n):
            if graph[i][j] == -100:
                graph[i][j] = -1
    return count

def backup():
    dfs(0, 0, -1, 0)

cycle = 0
result = []
while True:
    cycle += 1
    remove()
    # print(graph)
    cnt = melt()
    result.append([cycle, cnt])
    backup()
    # print(cnt)
    if cnt == 0:
        break
result.pop()
print(result[-1][0])
print(result[-1][1])
