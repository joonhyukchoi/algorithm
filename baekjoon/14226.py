import sys
# 클립보드도 인덱스에 넣고 bfs
from collections import deque
s = int(input())
ans = [0] * (1001)
q = deque()
q.append((1, 0, 0))
while q:
    now, clip, dist = q.popleft()
    if ans[now] == 0:
        ans[now] = dist
        if clip != 0:
            q.append((now + clip, clip, dist + 1))
        q.append((now, now, dist + 1))
        q.append((now - 1, clip, dist + 1))


print(ans[s])


