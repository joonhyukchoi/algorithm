import sys

inp = sys.stdin.readline
n, l = map(int, inp().split())
# print(n, l)
pools = []
for i in range(n):
    pools.append(list(map(int, inp().split())))
pools.sort(key = lambda x : x[0])
# print(pools)

bef = 0
count = 0
for i in range(n):
    x, y = pools[i]
    next = x
    if next < bef:
        next = bef
    while next < y:
        next += l
        count += 1
    bef = next
print(count)