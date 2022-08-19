def solution(n, k, cmd):
    answer = ''
    pos = k
    ans_list = [True] * n
    stack = []

    def posUp(pos, size):
        while size > 0:
            pos += 1
            if ans_list[pos] == True:
                size -= 1
        return pos

    def posDown(pos, size):
        while size > 0:
            pos -= 1
            if ans_list[pos] == True:
                size -= 1
        return pos
        
    def checkMax(pos):
        for i in range(pos, n):
            if ans_list[i] == True:
                return False
        return True

    for el in cmd:
        # print(pos, ans_list)
        if el[0] == 'D':
            el = el.replace("D ", '')
            pos = posUp(pos, int(el))
        elif el[0] == 'C':
            stack.append(pos)
            ans_list[pos] = False
            if checkMax(pos):
                pos = posDown(pos, 1)
            else:
                pos = posUp(pos, 1)
        elif el[0] == 'U':
            el = el.replace("U ", '')
            pos = posDown(pos, int(el))
        else:
            regen_pos = stack.pop()
            ans_list[regen_pos] = True
    for i in range(n):
        if ans_list[i] == True:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n, k, cmd)