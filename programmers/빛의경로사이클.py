
def solution(grid):
    dy = (1, 0, -1, 0)
    dx = (0, -1, 0, 1)
    
    answer = []
    ly, lx = len(grid), len(grid[0])
    
    flag = [[[False] * 4 for _ in range(lx)] for _ in range(ly)]
    
    for y in range(ly):
        for x in range(lx):
            for d in range(4):
                if flag[y][x][d]:
                    continue
                count = 0
                ny, nx = y, x
                while not flag[ny][nx][d]:
                    flag[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == 'S':
                        pass
                    elif grid[ny][nx] == 'L':
                        d = (d - 1) % 4
                    elif grid[ny][nx] == 'R':
                        d = (d + 1) % 4
                    
                    ny = (ny + dy[d]) % ly
                    nx = (nx + dx[d]) % lx
                answer.append(count)
        answer.sort()
    return answer