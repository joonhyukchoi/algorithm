from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    for i in range((len(q1) + len(q2)) * 2):
        if sum_q1 > sum_q2:
            top = q1.popleft()
            q2.append(top)
            sum_q1 -= top
            sum_q2 += top
            count += 1
        elif sum_q1 < sum_q2:
            top = q2.popleft()
            q1.append(top)
            sum_q1 += top
            sum_q2 -= top
            count += 1
        else:
            return count
    return -1