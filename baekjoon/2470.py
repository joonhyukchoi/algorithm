import sys
n = int(input())
lq = list(map(int,sys.stdin.readline().split()))
lq.sort()
start = 0
end = len(lq) - 1
sol = [lq[start], lq[end]]
while start < end:
    temp = lq[start] + lq[end]
    if abs(sum(sol)) > abs(temp):
        sol = [lq[start], lq[end]]
    if temp > 0:
        end -= 1
    elif temp < 0:
        start += 1
    else:
        break
print(sol[0], sol[1])

