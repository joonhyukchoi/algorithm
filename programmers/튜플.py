from collections import Counter
# from collections import deque

def solution(s):
    answer = []
    s = s[1:-1]
    s = s.replace('},{','}{')
    # 괄호의 개수를 카운트하는 함수 없을까?
    # result = [[] * Counter(s)['{']]
    result = []
    temp = []
    tempstr = ''
    for el in s:
        if el == '{':
            continue
        if el == '}':
            temp.append(int(tempstr))
            tempstr = ''
            result.append(temp)
            temp = []
        elif el == ',':
#             ord 는 문자열을 숫자로, chr 은 숫자를 아스키 문자열로
            # print(el, 48 <= ord(el) <= 57)
            temp.append(int(tempstr))
            tempstr = ''
        else:
            # print(el, 48 <= ord(el) <= 57)
            tempstr += el
    # print(result)
    result.sort(key = lambda x : -len(x))
    # print(result)
    for i in range(len(result)):
        templist = result.pop()
        for el in templist:
            if el not in answer:
                answer.append(el)
                break
    # sl = list(s)
    # print(sl)
    # sl.sort(key = lambda x : len[x])
    # print(s)
    return answer
