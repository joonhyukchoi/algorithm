import sys
import bisect
inp = sys.stdin.readline
n, m = map(int, inp().split())
course = list(map(int, inp().split()))
# course.sort()
s = [0]
temp = 0
for el in course:
    temp += el
    s.append(temp)
left = 0
right = s[-1]
ans = s[-1]
while left <= right:
    mid = (left + right) // 2
    bef = 0
    count = 1
    index = 0
    while index < len(s):
        index = bisect.bisect_left(s, bef + mid)
        bef = s[index]
        count += 1
        if index == len(s) - 1:
            count += 1
    if count > m:
        left = mid + 1
    else:
        ans = min(ans, mid)
        right = mid - 1
print(ans)
