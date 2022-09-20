from collections import deque

def bfs(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                x, y = i, j
                flag = [[False] * 5 for _ in range(5)]
                queue = deque()
                queue.append((x, y, 0))
                flag[x][y] = True
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                while queue:
                    x_now, y_now, dist = queue.pop()
                    if dist >= 2:
                        continue
                    for i in range(4):
                        nx = x_now + dx[i]
                        ny = y_now + dy[i]
                        if 0 <= nx <= 4 and 0 <= ny <= 4 and flag[nx][ny] == False:
                            if place[nx][ny] == 'X':
                                continue
                            elif place[nx][ny] == 'P' and dist <= 1:
                                return False
                            else:
                                flag[nx][ny] = True
                                queue.append((nx, ny, dist + 1))
    return True
def solution(places):
    answer = []
    for place in places:
        if bfs(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer