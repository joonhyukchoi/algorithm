import sys
inp = sys.stdin.readline
n = int(inp())
INF = 10**9
p = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        p[i] = 1
        continue
    if i == 2:
        p[i] = 2
        continue
    p[i] = p[i-1]
    if i % 2 == 0:
        p[i] += p[i // 2]
print(p[n] % 1000000000)