# from collections import deque
# def solution(people, limit):
#     q = deque()
#     people.sort()
#     for el in people:
#         q.append(el)
#     answer = 0
#     while q:
#         big = q.pop()
#         if q and big + q[0] <= limit:
#             q.popleft()
#         answer += 1
#     return answer
S = 0
S |= 1 << 10
S |= 1 << 4
# S &= ~(1 << 4)
print(S & 1 << 4)
test = [1, 2, 3]
s1 = set(test)
s2 = set()
s1.add(1)
s1.add(4)
s2.add(3)
print(s1)

import collections
import itertools

outpuet = collections.Counter([1,2,3,3,4])
print(outpuet.most_common(1))