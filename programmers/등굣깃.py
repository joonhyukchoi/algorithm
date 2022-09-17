def solution(m, n, puddles):
    answer = 0
    graph = [[0] * m for _ in range(n)]
    for puddle in puddles:
        x, y = puddle
        graph[y - 1][x - 1] = -1
    graph[0][0] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                continue
            if i - 1 >= 0 and graph[i - 1][j] != -1:
                graph[i][j] += graph[i - 1][j]
            if j - 1 >= 0 and graph[i][j - 1] != -1:
                graph[i][j] += graph[i][j - 1]
    # print(graph)
    answer = graph[n - 1][m - 1] % 1000000007
    return answer