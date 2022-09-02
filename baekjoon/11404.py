import sys
inp = sys.stdin.readline
n = int(inp())
m = int(inp())
INF = 10**9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, d = map(int, inp().split())
    if graph[a][b] != 0:
        if d < graph[a][b]:
            graph[a][b] = d

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if graph[x][y] == INF:
            print('0', end = ' ')
            continue
        print(graph[x][y], end = ' ')
    print()
