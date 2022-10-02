import sys
inp = sys.stdin.readline
s = ''
result = []
while s != 'end':
    s = inp().strip()
    if s != 'end':
        numX = 0
        numO = 0
        for i in range(9):
            if s[i] == 'X':
                numX += 1
            elif s[i] == 'O':
                numO += 1
        graph = []
        for i in range(3):
            temp = []
            for j in range(i * 3, (i + 1) * 3):
                temp.append(s[j])
            graph.append(temp)
        count_X = 0
        count_O = 0
        # 가로방향 확인
        for i in range(3):
            X = 0
            O = 0
            for j in range(2):
                if graph[i][j] == graph[i][j + 1] and graph[i][j] != '.':
                    if graph[i][j] == 'X':
                        X += 1
                    else:
                        O += 1
                else:
                    break
            if X == 2:
                count_X += 1
            elif O == 2:
                count_O += 1
        # 세로방향 확인
        for i in range(3):
            X = 0
            O = 0
            for j in range(2):
                if graph[j][i] == graph[j + 1][i] and graph[j][i] != '.':
                    if graph[j][i] == 'X':
                        X += 1
                    else:
                        O += 1
                else:
                    break
            if X == 2:
                count_X += 1
            elif O == 2:
                count_O += 1
        # 대각선방향 확인
        if graph[0][0] == graph[1][1] == graph[2][2] and graph[0][0] != '.':
            if graph[0][0] == 'X':
                count_X += 1
            else:
                count_O += 1 
        if graph[2][0] == graph[1][1] == graph[0][2] and graph[2][0] != '.':
            if graph[2][0] == 'X':
                count_X += 1
            else:
                count_O += 1 
        # print(count_X, count_O)
        if (count_X == 1 and count_O == 0 and numX == numO + 1) \
            or (count_X == 0 and count_O == 1 and numX == numO) \
            or (count_X == 0 and count_O == 0 and numX == 5 and numO == 4) \
            or (count_X == 2 and count_O == 0 and numX == 5 and numO == 4):
            result.append('valid')
        else:
            result.append('invalid')
for i in result:
    print(i)