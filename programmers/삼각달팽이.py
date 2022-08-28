def solution(n):
    answer = []
    all = [[0] * (i + 1) for i in range(n + 1)]
    cnt = 0
    boundary = n
    i, j = 0, 1
    while cnt < n * (n + 1) / 2:
#         /
        for _ in range(boundary):
            cnt += 1
            i += 1
            all[i][j] = cnt
        if cnt >= n * (n + 1) / 2:
            break
        boundary -= 1
#         _
        for _ in range(boundary):
            cnt += 1
            j += 1
            all[i][j] = cnt
        if cnt >= n * (n + 1) / 2:
            break
        boundary -= 1
#         \
        for _ in range(boundary):
            cnt += 1
            i -= 1
            j -= 1
            all[i][j] = cnt
        if cnt >= n * (n + 1) / 2:
            break
        boundary -= 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            answer.append(all[i][j])
    return answer