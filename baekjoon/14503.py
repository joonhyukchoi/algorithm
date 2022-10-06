import sys
inp = sys.stdin.readline

r, c = map(int, inp().split())
start_x, start_y, direction = map(int, inp().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
for i in range(r):
    graph.append(list(map(int, inp().split())))
    
def dfs(x, y, direction):
    count = 0
    for i in range(-1, -5, -1):
        ndirection = (direction + i) % 4
        if ndirection < 0:
            ndirection += 4
        nx = x + dx[ndirection]
        ny = y + dy[ndirection]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            dfs(nx, ny, ndirection)
            break
        elif 0 <= nx < r and 0 <= ny < c and (graph[nx][ny] == 2 or graph[nx][ny] == 1):
            count += 1
    if count >= 4:
        inverse_direction = (direction + 2) % 4
        nx = x + dx[inverse_direction]
        ny = y + dy[inverse_direction]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 2:
            dfs(nx, ny, direction)
        else:
            pass

graph[start_x][start_y] = 2
dfs(start_x, start_y, direction)
clean = 0
# print(graph)
for i in range(r):
    for j in range(c):
        if graph[i][j] == 2:
            clean += 1
print(clean)
