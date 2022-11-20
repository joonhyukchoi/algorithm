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