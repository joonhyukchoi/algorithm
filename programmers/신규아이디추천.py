def solution(new_id):
    answer = ''
    answer = new_id.lower()
    i = 0
    temp = ''
    while i < len(answer):
        if answer[i].isalnum() or answer[i] == '-' or answer[i] == '_' or answer[i] == '.':
            # if answer[i] == '.':
            #     temp += answer[i]
            # else:
            #     if len(temp) >= 2:
            #         answer = answer.replace(temp, '.')
            #     temp = ''
            i += 1
        else:
            answer = answer.replace(answer[i], '')
    # print(answer)
    # temp = '.'
    for i in range(500):
        answer = answer.replace('..', '.')
    print(answer)
    if answer and answer[0] == '.':
        answer = answer[1:]
    while answer and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]
    return answer