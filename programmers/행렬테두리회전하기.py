def solution(rows, columns, queries):
    answer = []
    array = [[j + rows * i for j in range(1, columns + 1)] for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = query
        dx = x2 - x1
        dy = y2 - y1
        axisx = [x1, x2, x2, y2]
        axisy = [y1, y1, y2, y2]
        my = [1, 0, -1, 0]
        mx = [0, -1, 0, 1]
        distances = [dy, dx, dy, dx]
        x, y = x1, y1
        for i in range(4):
            first = array[axisx[i]][axisy[i]]
            print(first)
            for dis in range(distances[i]):
                print(x, y, mx[i], my[i], dis)
                if dis == 0:
                    temp = array[x + mx[i]][y + my[i]]
                    array[x + mx[i]][y + my[i]] = first
                    first = temp
                else:
                    x = x + mx[i] 
                    y = y + my[i]
                    temp = array[x + mx[i]][y + my[i]]
                    array[x + mx[i]][y + my[i]] = first
                    first = temp
            
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))