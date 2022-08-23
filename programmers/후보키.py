# combination 튜플 전체 케이스를 빠트려서 크게삽질함
from itertools import combinations
def Parse(rel, x):
    tempStr = ''
    for i in x:
        tempStr += rel[i]
    return tempStr

def check(rel, x):
    temp = [Parse(rel[0], x)]
    for el in rel:
        if el == rel[0]:
            continue
        if Parse(el, x) in temp:
            return False
        temp.append(Parse(el, x))
    return True
            
def interCheck(x, answer):
    if len(answer) == 0:
        return False
    for el in answer:
        # print(set(x) & el, set(x), el)
        if set(x) & el == el:
            return True
    return False

def solution(relation):
    case = len(relation[0])
    count = 0
    cases = [i for i in range(case)]
    answer = []
    for i in range(case + 1):
        for x in combinations(cases, i):
            if interCheck(x, answer):
                continue
            if check(relation, x):
                answer.append(set(x))
                count += 1
    return count