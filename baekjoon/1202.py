import sys
import heapq

sys.setrecursionlimit(10**6)
inp = sys.stdin.readline

n, k = map(int, inp().split())
jews = []
temp = []
for i in range(n):
    m, v = map(int, inp().split())
    heapq.heappush(jews, (m, v))

bags = []
for i in range(k):
    bags.append(int(inp()))
bags.sort()
sum = 0
for i in range(k):
    while jews and jews[0][0] <= bags[i]:
        nm, nv = heapq.heappop(jews)
        heapq.heappush(temp, (-nv, nm))
    if temp:
        sum += -heapq.heappop(temp)[0]
print(sum)
