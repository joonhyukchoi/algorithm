import sys
import heapq

inp = sys.stdin.readline
n = int(inp())
homes = []
last = []
for _ in range(n):
    a, b = map(int, inp().split())
    if a < b:
        last.append(b)
        heapq.heappush(homes, (b, a))
    else:
        last.append(a)
        heapq.heappush(homes, (a, b))
l = int(inp())
temp = []
maxl = 0
for i in sorted(set(last)):
    while homes and homes[0][0] <= i:
        b, a = heapq.heappop(homes)
        if i - l <= a:
            heapq.heappush(temp, (a, b))
    while temp and temp[0][0] < i - l:
        heapq.heappop(temp)
    maxl = max(maxl, len(temp))
    # 시간초과
    # for i in range(len(temp)):
    #     heapq.heappush(homes, temp.pop())
print(maxl)