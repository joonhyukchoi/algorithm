import heapq

def solution(jobs):
    heap = []
    heap2 = []
    for job in jobs:
        heapq.heappush(heap, job)
    last = 0
    sum = 0
    while heap:
#         시간안에 들어온 디스크 요청 heap2에 push, 작업시간 기준으로 push
        while heap and heap[0][0] <= last:
            temp_min_element = heapq.heappop(heap)
            heapq.heappush(heap2, [temp_min_element[1], temp_min_element[0]])
#         작업시간이 가장 작은 요소 1개 pop        
        if heap2:
            min_element = heapq.heappop(heap2)
            last = last + min_element[0]
            sum += last - min_element[1]
        else:
#             디스크가 작업수행이 없을 때
            last += 1
#             heap2 요소들 다시 heap으로 push
        while heap2:
            temp = heapq.heappop(heap2)
            heapq.heappush(heap, [temp[1], temp[0]])
    return sum // len(jobs)