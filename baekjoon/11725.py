import sys
sys.setrecursionlimit(10**6)
inp = sys.stdin.readline
n = int(inp())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
flag = [True] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, inp().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    flag[node] = False
    for son in graph[node]:
        if flag[son]:
            parent[son] = node
            dfs(son)
dfs(1)
for i in range(2, n + 1):
    print(parent[i])