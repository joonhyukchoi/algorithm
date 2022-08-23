from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    answer = []
    speedQueue = deque(speeds)
    while len(queue) > 0:
        length = len(queue)
        for i in range(length):
            queue[i] += speedQueue[i]
        count = 0
        print(queue)
        if queue[0] >= 100:
            while len(queue) > 0 and queue[0] >= 100:
                print(queue)
                queue.popleft()
                speedQueue.popleft()
                count += 1
            answer.append(count)
    
    return answer
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))