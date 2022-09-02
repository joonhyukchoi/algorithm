# import bisect
import sys
inp = sys.stdin.readline

n, c = map(int, inp().split())
homes = []
for i in range(n):
    homes.append(int(inp()))
homes.sort()

start = 1
end = homes[-1] - homes[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = homes[0]
    count = 1

    for i in range(1, n):
        if homes[i] >= value + mid:
            value = homes[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
# bisect.bisect_left()
