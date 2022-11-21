import copy

def solution(n, lighthouse):
    answer = 0
    count = n
    network = [[0, num] for num in range(n + 1)]
    networkVal = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for arr in lighthouse:
        a, b = arr
        network[a][0] += 1
        network[b][0] += 1
        networkVal[a] += 1
        networkVal[b] += 1
        graph[a].append(b)
        graph[b].append(a)
    network.sort()
    # print(networkVal)
    while True:
        # index = (network.pop())[1]
        index = networkVal.index(max(networkVal))
        # print(index)
        networkVal[index] = 0
        count -= 1
        for el in graph[index]:
            networkVal[el] -= 1
            if networkVal[el] == 0:
                count -= 1
        # print('count', count)
        answer += 1
        if count <= 0:
            break
    return answer


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
import sys
sys.setrecursionlimit(10**6)

def dfs(visit, parent, graph):
    dfs.dp[visit][1] = 1
    for route in graph[visit]:
        if route != parent:
            dfs(route, visit, graph)
            dfs.dp[visit][1] += min(dfs.dp[route][0], dfs.dp[route][1])
            dfs.dp[visit][0] += dfs.dp[route][1]

def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for l in lighthouse:
        i, j = sorted(l)
        graph[i].append(j)
        graph[j].append(i)
    dfs.dp = [[0, 0] for _ in range(n + 1)]
    dfs(1, 1, graph)
    return min(dfs.dp[1])

    # 그래프를 생성한다.
# 단말노드를 찾는다
# 연결된 등대를 밝힌다.
# 불을 밝힌 등대를 그래프에서 지운다.
# 다시 단말노드를 찾는다.

from collections import defaultdict, deque 
def solution(n, lighthouse):
    lighted = [0 for _ in range(n+1)]
    excepted = set()

    while 1:
        # 그래프 생성
        graph = defaultdict(list)
        for a,b in lighthouse:
            # 불을 밝힌 등대는 그래프에서 지운다.
            if a not in excepted and b not in excepted:
                graph[a].append(b)
                graph[b].append(a)
        #print(graph)
        # 그래프가 그려지 않으면 종료
        if not graph:
            break

        # 단말노드를 찾아 연결된 등대를 밝힌다.
        for k,v in graph.items():
            if len(v) == 1 and lighted[k] != 1:
                lighted[v[0]] = 1
                excepted.add(v[0])

    return sum(lighted)