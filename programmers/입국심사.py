# import heapq

# def solution(n, times):
#     answer = 0
#     heap = []
#     for time in times:
#         heapq.heappush(heap, (time, 0))
#     count = 0
#     while count != n:
#         el1, el2 = heapq.heappop(heap)
#         heapq.heappush(heap, (el1 + el1 - el2, el1))
#         count += 1
#         # print(heap[0][0], heap[0][1])
#         if count == n:
#             return el1
#             break
            
def solution(n, times):
    left, right = 1, max(times) * n
    while left < right:
        mid = (right + left)// 2
        count = 0
        for time in times:
            count += mid // time
            
            if count >= n:
                break
        if count >= n:
            right = mid
        else:
            left = mid + 1
    return left
    