from bisect import bisect_left
def solution(target):
    answer = [0, 0]
    score = []
    for i in range(1, 4):
        for j in range(1, 21):
            if i*j not in score:
                score.append(i * j)
    score.append(50)
    score.sort()
    while target > 0:
        answer[0] += 1
        if target > 50 :
            if target != 51 and target != 54  \
            and target != 57 and target != 60:
                target -= 50
                answer[1] += 1
            else:
                target = 0
        else:
            if target <= 20 or target == 50:
                answer[1] += 1
            if target not in score:
                if target <= 40:
                    answer[1] += 1
                    target -= 20
                else:
                    target -= 40
            else:
                target = 0
        print(score)
    return answer