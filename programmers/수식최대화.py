from itertools import permutations
import copy
def solution(expression):
    answer = 0
    def dfs(numstr, operations, cnt):
        if cnt == 2:
            return str(eval(numstr))
        temp = numstr.split(operations[cnt])
        output = []
        for n in temp:
            output.append(dfs(n, operations, cnt + 1))
        return str(eval(operations[cnt].join(output)))
    max_val = 0
    for operations in permutations(['+', '*', '-'], 3):
        answer = max(answer, abs(int(dfs(expression, operations, 0))))
    return answer