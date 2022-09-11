from itertools import combinations 
def solution(orders, course):
    a = []
    def check_include(answer, el):
        for i in answer:
            if set(el) & set(i) == set(el):
                return True
        return False
    
    course.sort(reverse = True)
    for order in orders:
        for n in course:
            templist = list(combinations(order, n))
            maxcnt = 0
            answer = []
            for el in templist:
                cnt = 0
                el = sorted(el)
                if el in a:
                    continue
                for o in orders:
                    s1 = set(el)
                    s2 = set(o)
                    if s1 & s2 == s1:
                        cnt += 1
                if cnt >= 2:
                    answer.append([cnt, el])
            answer.sort(reverse = True)
            if answer:
                temp = answer[0][0]
                # print(answer)
                for el in answer:
                    if el[0] == temp and el[1] not in a:
                        a.append(el[1])
    ans = []
    # for a in answer:
    #     ans.append(''.join(a))
    # ans.sort()
    print(a)
    return ans