def solution(n):
    answer = 0
    cross = (2 * n - 1)
    flag1 = [True] * n
    # flag2 = [True] * n
    flag3 = [True] * cross
    flag4 = [True] * cross
    def queen(i, j, cnt):
        if cnt == n:
            nonlocal answer
            answer += 1
        for i in range(n):
            if flag1[i] and flag3[i + j] and flag4[cross // 2 + i - j]:
                flag1[i] = flag3[i + j] = flag4[cross // 2 + i - j] = False
                queen(i, j + 1, cnt + 1)
                flag1[i] = flag3[i + j] = flag4[cross // 2 + i - j] = True
    queen(0, 0, 0)
    return answer