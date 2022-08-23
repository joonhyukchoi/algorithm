import copy
answer = 0

def solution(numbers, target):
    numCnt = len(numbers)
    operations = ['+', '-']
    def dfs(curStr, target, cnt):
        global answer
        if cnt == numCnt:
            if eval(curStr) == target:
                answer += 1
            return
        for oper in operations:
            # print(curStr)
            temp = copy.deepcopy(curStr)
            curStr += oper
            curStr += str(numbers[cnt])
            dfs(curStr, target, cnt + 1)
            curStr = copy.deepcopy(temp)
    dfs('', target, 0)
    return answer