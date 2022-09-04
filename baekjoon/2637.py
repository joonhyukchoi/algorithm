import sys
from collections import deque, defaultdict

inp = sys.stdin.readline
n = int(inp())
m = int(inp())
check = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
flag = [False] * (n + 1)
for _ in range(m):
    x, y, k = map(int, inp().split())
    graph[x].append((y, k))
    check[y] += 1

q = deque()
hash = defaultdict(int)
for i in range(1, n + 1):
    if check[i] == 0:
        q.append(i)
        hash[i] = 1
    else:
        hash[i] = 0
result = []
while q:
    now = q.popleft()
    if graph[now]:
        for y, cost in graph[now]:
            check[y] -= 1
            hash[y] += cost * hash[now]
            if check[y] == 0:
                q.append(y)
    else:
        result.append((now, hash[now]))

result.sort()
for i, val in result:
    print(i, val)


