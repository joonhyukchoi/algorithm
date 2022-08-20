
def solution(gems):
    myset = list(set(gems))
    flag = [0] * len(myset)
    sol = []
    count = 0
    minv = 1000000
    for i, el in enumerate(gems):
        if flag[myset.index(el)] == 0:
            count = count + 1
        flag[myset.index(el)] = i + 1
        # if 0 not in flag:
        #     sol.append([min(flag), max(flag)])
        if count == len(set(gems)) and (max(flag) - min(flag)) < minv:
            sol.append([min(flag), max(flag)])
            minv = (max(flag) - min(flag))
    minv = 1000000
    solindex = 0
    for i, el in enumerate(sol):
        if el[1] - el[0] == 0:
            solindex = i
            break
        if el[1] - el[0] < minv:
            solindex = i
            minv = el[1] - el[0]
    
    return sol[solindex]