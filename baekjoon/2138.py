import sys
import copy
inp = sys.stdin.readline
n = int(inp())
start, target = [], []
start_str = inp().rstrip()
target_str = inp().rstrip()
for i in range(n):
    start.append(int(start_str[i]))
    target.append(int(target_str[i]))

# first trial
count = 0
temp = copy.deepcopy(start)
temp[0] = 1 - temp[0]
temp[1] = 1 - temp[1]
count += 1
for i in range(1, n):
    if temp[i - 1] != target[i - 1]:
        for j in range(-1, 2):
            if i + j <= n - 1:
                temp[i + j] = 1 - temp[i + j]
        count += 1
if temp == target:
    print(count)
else:
    # second trial
    count = 0
    temp = copy.deepcopy(start)
    temp[0] = 1 - temp[0]
    temp[1] = 1 - temp[1]
    count += 1
    for i in range(1, n):
        if temp[i - 1] != target[i - 1]:
            for j in range(-1, 2):
                if i + j <= n - 1:
                    temp[i + j] = 1 - temp[i + j]
            count += 1
    if temp == target:
        print(count)
    else:
        print(-1)