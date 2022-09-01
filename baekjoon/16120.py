from operator import truediv
import sys
from collections import deque

inp = sys.stdin.readline
instr = inp().strip()
ppap = deque([])
stack = []
for el in instr:
    ppap.append(el)
i = 0
def checkSame(stack):
    if len(stack[-4:]) == 4:
        if stack[0] == 'P' and stack[1] == 'P' and stack[2] == 'A' and stack[3] == 'P':
            return True
    return False

# string replace 사용하니 시간초과!
while ppap:
    bottom = ppap.popleft()
    stack.append(bottom)
    while checkSame(stack[-4:]):
        for _ in range(3):
            stack.pop()
if len(stack) == 1 and stack[0] == 'P':
    print('PPAP')
else:
    print('NP')
