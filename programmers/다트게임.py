def solution(dartResult):
    answer = 0
    result = []
    operations = []
    temp = ''
    for w in dartResult:
        if w.isdigit():
            temp += w
        else:
            if temp != '':
                result.append(int(temp))
                temp = ''
            operations.append(w)
    answer_list = []       
    for operation in operations:
        if operation == 'S':
            temp = result.pop(0)
            answer_list.append(temp)
        elif operation == 'D':
            temp = result.pop(0)
            temp = temp * temp
            answer_list.append(temp)
        elif operation == 'T':
            temp = result.pop(0)
            temp = temp * temp * temp
            answer_list.append(temp)
        elif operation == '*':
            if len(answer_list) >= 2:
                answer_list[-1] *= 2
                answer_list[-2] *= 2
            else:
                answer_list[-1] *= 2
        else:
            answer_list[-1] *= -1
    answer = sum(answer_list)
    return answer