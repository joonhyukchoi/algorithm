def solution(n, k, cmd):
    answer = ''
    pos = k
    stack = []
    ans_list = [True] * n
    def count_upward(pos):
        count = 0
        print('in counst_upward', stack)
        for el in stack:
            if el > pos:
                count += 1
        return count
    
    for el in cmd:
        print('pos:',pos)
        if el[0] == 'D':
            el = el.replace("D ", '')
            pos += int(el)
        elif el[0] == 'C':
            stack.append(pos)
            # print('in pos:',n, pos, count_upward(pos))
            if n - pos - len(stack) == 0:
                pos = pos - 1
        elif el[0] == 'U':
            el = el.replace("U ", '')
            pos -= int(el)
        else:
            live = stack.pop()
            if live < pos:
                pos += 1
    for el in stack:
        ans_list[el] = False
    for i in range(n):
        if ans_list[i] == True:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer