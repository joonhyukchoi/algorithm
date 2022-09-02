def solution(sales, links):
    answer = 0
    count = len(sales)
    graph = [[] for _ in range(count + 1)]
    d = [[1000000, 1000000] for _ in range(count + 1)]
    sum_child = [0] * (count + 1)
    for link in links:
        a, b = link
        graph[a].append(b)
    sales.insert(0, 0)
    def dp(n, index):
        if d[n][index] != 1000000:
            return d[n][index]
        check = False
        minval = 1000000
        tempSum = 0
        if graph[n]:
            for k in graph[n]:
                tempSum += min(dp(k, 0), dp(k, 1))
                if d[k][0] > d[k][1]:
                    check = True
                else:
                    if minval > d[k][1] - d[k][0]:
                        minval = d[k][1] - d[k][0]
            sum_child[n] = tempSum
        else:
            d[n][0] = 0
            d[n][1] = sales[n]
            return d[n][index]
        if index == 0:
            if check:
                d[n][0] = sum_child[n]
            else:
                d[n][0] = sum_child[n] + minval
            return d[n][index]

        elif index == 1:
            d[n][1] = sales[n] + sum_child[n]
            return d[n][index]
    return min(dp(1, 0),dp(1, 1))