import sys
inp = sys.stdin.readline

n = int(inp())
stairs = [0] * (3)
sum = [0] * (n + 4)

for i in range(n):
    stairs.append(int(inp()))
# print(',')
for i in range(3, n + 3):
    sum[i] = stairs[i] + max(sum[i - 2], stairs[i - 1] + sum[i - 3])
# for i in range(n + 3):
#     print(sum[i])

print(sum[n + 2])