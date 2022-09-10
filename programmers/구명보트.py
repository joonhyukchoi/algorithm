from collections import deque
def solution(people, limit):
    q = deque()
    people.sort()
    for el in people:
        q.append(el)
    answer = 0
    while q:
        big = q.pop()
        if q and big + q[0] <= limit:
            q.popleft()
        answer += 1
    return answer