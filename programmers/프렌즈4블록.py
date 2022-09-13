import copy
def solution(m, n, board):
    temp = []
    for b in board:
        temp.append(list(b))
    board = copy.deepcopy(temp)
    answer = 0
    refresh = []
    score = 0
    while score < m*n:
        for i in range(m):
            for j in range(n):
                if i + 1 < m and j + 1 < n and board[i][j] != 'X':
                    if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                        refresh.append([i, j])
        # print(refresh)
        if len(refresh) == 0:
            break
        while refresh:
            x, y = refresh.pop(0)
            if board[x][y] != 'X':
                score += 1
                board[x][y] = 'X'
            if board[x + 1][y] != 'X':
                score += 1
                board[x + 1][y] = 'X'
            if board[x][y + 1] != 'X':
                score += 1
                board[x][y + 1] = 'X'
            if board[x + 1][y + 1] != 'X':
                score += 1
                board[x + 1][y + 1] = 'X'
        # print(score)
        for i in range(n):
            cnt = 0
            for j in range(m - 1, -1, -1):
                if board[j][i] == 'X':
                    cnt += 1
                elif cnt > 0:
                    board[j][i], board[j + cnt][i] = board[j + cnt][i], board[j][i]
    return score