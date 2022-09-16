import heapq

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

def solution(N, road, K):
    answer = 0
    INF = 10**9
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    flag = [False] * (N + 1)
    for vertex in road:
        a, b, dis = vertex
        graph[a].append((b, dis))
        graph[b].append((a, dis))
    heap = []
    heapq.heappush(heap, (0, 1))
    distance[1] = 0
    while heap:
        now_d, now_pos = heapq.heappop(heap)
        if distance[now_pos] < now_d or flag[now_pos]:
            continue
        flag[now_pos] = True 
        for el in graph[now_pos]:
            sum_d = now_d + el[1]
            if sum_d < distance[el[0]]:
                distance[el[0]] = sum_d
                heapq.heappush(heap, (sum_d, el[0]))
    for n in distance:
        if n <= K:
            answer += 1
    return answer

print(solution(N, road, K))