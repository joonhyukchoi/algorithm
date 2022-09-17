import heapq
from collections import deque
import copy
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def solution(board, r, c):
    answer = 0
    heap = []
    target = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                target += 1
    target //= 2
    min_num = 10**9
    def find_couple(nx, ny, cnt, temp):
        n_nx = nx
        n_ny = ny
        for i in range(4):
            for j in range(4):
                if i == nx and j == ny:
                    continue
                if board[i][j] == board[nx][ny]:
                    n_nx = i
                    n_ny = j
        q = deque()
        q.append((0, nx, ny))
        while q:
            count, x, y = q.popleft()
            if x == n_nx and y == n_ny:
                return (count + 1, x, y)
            for i in range(4):
                newx = x + dx[i]
                newy = y + dy[i]
                if 0 <= newx < 4 and 0 <= newy < 4:
                    q.append((count + 1, newx, newy))
                while 0 <= newx < 4 and 0 <= newy < 4 and (board[newx][newy] == 0 or board[newx][newy] in flag):
                    # print(newx, newy)
                    newx = newx + dx[i]
                    newy = newy + dy[i]
                    if (count + 1, newx, newy) not in q:
                        q.append((count + 1, newx, newy)) 
    # 찾은 갯수, 좌표 x, y, 카운트
    heapq.heappush(heap, (0, r, c, 0, []))
    while heap:
        got, x, y, cnt, flag = heapq.heappop(heap)
        if got == target:
            min_num = min(min_num, cnt)
            continue
        if cnt >= min_num:
            continue
        # 4방향 한칸 움직임
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if board[nx][ny] in flag:
                    continue
                temp = copy.deepcopy(flag)
                if board[nx][ny] != 0:
                    temp.append(board[nx][ny])
                    # 움직임 + 엔터 = cnt + 2
                    nx, ny, cnt = find_couple(nx, ny, cnt + 2, temp)
                    heapq.heappush(heap, (-(got + 1), nx, ny, cnt, temp))
                else:
                    # 움직임 = cnt + 1
                    heapq.heappush(heap, (-got, nx, ny, cnt + 1, temp))
        # 4방향 점프
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < 4 and 0 <= ny < 4 and (board[nx][ny] == 0 or board[nx][ny] in flag):
                # print(nx, ny, i)
                nx = nx + dx[i]
                ny = ny + dy[i]
            # 위 네방향 로직과 로직 동일
            if 0 <= nx < 4 and 0 <= ny < 4:
                if board[nx][ny] in flag:
                    continue
                temp = copy.deepcopy(flag)
                if board[nx][ny] != 0:
                    temp.append(board[nx][ny])
                    # 움직임 + 엔터 = cnt + 2
                    nx, ny, cnt = find_couple(nx, ny, cnt + 2, temp)
                    heapq.heappush(heap, (-(got + 1), nx, ny, cnt, temp))
                else:
                    # 움직임 = cnt + 1
                    heapq.heappush(heap, (-got, nx, ny, cnt + 1, temp))
    return answer
board =[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
solution(board, r, c)