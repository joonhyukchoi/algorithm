import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp())
m = int(inp())
string = inp().strip()
p = ''
for i in range(n):
    p += 'IO'
p += 'I'

# 아래와 같은 방법은 시간초과
# count = 0
# for i in range(m - n - 1):
#     if string[i:i + 2*n + 1] == p:
#         count += 1
# print(count)

# IOI를 단위로 비교
count = 0
Pattern = 0
i = 1
while i < m - 1:
  if string[i - 1] == 'I' and string[i] == 'O' and string[i + 1] == 'I':
    Pattern += 1
    if Pattern == n:
      Pattern -= 1
      count += 1   
    i += 1
  else:
    Pattern = 0
  i += 1
print(count)