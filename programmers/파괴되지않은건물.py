

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
result = 10

def solution(board, skill):
    answer = 0
    #  4 * 5 array
    n = len(board[0])
    m = len(board)
    newBoard = [[0] * (n + 1) for _ in range(m + 1)]
    for skill_one in skill:
        type, r1, c1, r2, c2, degree = skill_one
        if type == 1:
            newBoard[r1][c1] -= degree
            newBoard[r2 + 1][c2 + 1] -= degree
            newBoard[r2 + 1][c1] += degree
            newBoard[r1][c2 + 1] += degree
        else:
            newBoard[r1][c1] += degree
            newBoard[r2 + 1][c2 + 1] += degree
            newBoard[r2 + 1][c1] -= degree
            newBoard[r1][c2 + 1] -= degree

    for i in range(n):
        for j in range(m):
            newBoard[j][i + 1] += newBoard[j][i]

    for i in range(m):
        for j in range(n):
            newBoard[i + 1][j] += newBoard[i][j]

    for i in range(m):
        for j in range(n):
            board[i][j] += newBoard[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

solution(board, skill)