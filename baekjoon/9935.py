instring = input().strip()
bomb = input().strip()
stack = []
lenbomb = len(bomb)
for word in instring:
    stack.append(word)
    while stack and ''.join(stack[-lenbomb:]) == bomb:
        for _ in range(lenbomb):
            stack.pop()
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))