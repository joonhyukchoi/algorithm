def solution(rows, columns, queries):
    answer = []
    array = [[j + columns * i for j in range(1, columns + 1)] for i in range(rows)]
    for query in queries:
        x1, y1, x2, y2 = query
        dx = x2 - x1
        dy = y2 - y1
        axisx = [x2, x2, x1, x1]
        axisy = [y1, y2, y2, y1]
        mx = [0, -1, 0, 1]
        my = [1, 0, -1, 0]
        distances = [dy, dx, dy, dx]
        tempStart = array[axisx[0] - 1][axisy[0] - 1]
        tempMin = tempStart
        for i in range(4):
            startx, starty = axisx[i] - 1, axisy[i] - 1
            for dis in range(distances[i]):
                x = startx + dis * mx[i] 
                y = starty + dis * my[i]
                array[x][y] = array[x + mx[i]][y + my[i]]
                tempMin = min(tempMin, array[x][y])
                # print(x, y, mx[i], my[i], array)
        array[axisx[0] - 2][axisy[0] - 1] = tempStart
        answer.append(tempMin)
    return answer