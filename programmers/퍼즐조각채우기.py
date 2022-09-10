game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
from collections import defaultdict, deque
import copy
q = deque()
block_dict = defaultdict(list)
r = len(game_board)
c = len(game_board[0])
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def table_dfs(x, y, minmax, block_list):
    table[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and table[nx][ny] == 1:
            minmax[0] = min(minmax[0], nx)
            minmax[1] = min(minmax[1], ny)
            minmax[2] = max(minmax[2], nx)
            minmax[3] = max(minmax[3], ny)
            minmax[4] += 1
            block_list.append([nx, ny])
            table_dfs(nx, ny, minmax, block_list)

def move_and_align(new_list):
    for el in new_list[1]:
        el[0] -= new_list[0][0]
        el[1] -= new_list[0][1]

for i in range(r):
    for j in range(c):
        if table[i][j] == 1:
            minmax = [50, 50, 0, 0, 1]
            minmax[0] = min(minmax[0], i)
            minmax[1] = min(minmax[1], j)
            minmax[2] = max(minmax[2], i)
            minmax[3] = max(minmax[3], j)
            block_list = [[i,j]]
            table_dfs(i, j, minmax, block_list)
            new_list = []
            new_list.append(minmax[:4])
            new_list.append(block_list)
            move_and_align(new_list)
            block_dict[minmax[4]].append(new_list)

def board_dfs(x, y, minmax, block_list):
    game_board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and game_board[nx][ny] == 0:
            minmax[0] = min(minmax[0], nx)
            minmax[1] = min(minmax[1], ny)
            minmax[2] = max(minmax[2], nx)
            minmax[3] = max(minmax[3], ny)
            minmax[4] += 1
            block_list.append([nx, ny])
            board_dfs(nx, ny, minmax, block_list)

board = []
for i in range(r):
    for j in range(c):
        if game_board[i][j] == 0:
            minmax = [50, 50, 0, 0, 1]
            minmax[0] = min(minmax[0], i)
            minmax[1] = min(minmax[1], j)
            minmax[2] = max(minmax[2], i)
            minmax[3] = max(minmax[3], j)
            block_list = [[i,j]]
            board_dfs(i, j, minmax, block_list)
            new_list = []
            new_list.append(minmax[:4])
            new_list.append(block_list)
            move_and_align(new_list)
            board.append([minmax[4],new_list[1]])
print(block_dict)
print(board)
def compare_with_rotate(board_in, block_in, num):
    board_in_copied = copy.deepcopy(board_in)
    block_in_copied = copy.deepcopy(block_in)
    for i in range(3):
        cnt = 0
        for el in board_in_copied:
            print(board_in_copied)
            el[0], el[1] = el[1], r - 1 -el[0]
        for el in block_in_copied:
            if el in board_in_copied:
                cnt += 1
        if cnt == num:
            return True
    return False
answer = 0
for board_picked in board:
    num = board_picked[0]
    if len(block_dict[num]) == 0:
        continue
    else:
        for block_picked in block_dict[num]:
            if block_picked[0][-1] != -1 and compare_with_rotate(board_picked[1], block_picked[1], num):
                block_picked[0].append(-1)
                answer += num
                break
print(answer)