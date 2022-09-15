def solution(msg):
    answer = []
    idx = [-1]
    maxlen = 1
    for i in range(65, 91):
        # chr ord 기억하기
        idx.append(chr(i))
    # for i in range(len(msg)):
    i = 0
    while i < len(msg):
        for j in range(maxlen, -1, -1):
            # print(i, j, msg[i:i+j])
            if msg[i:i+j] in idx:
                idx.append(msg[i:i+j+1])
                maxlen = max(maxlen, len(msg[i:i+j+1]))
                answer.append(idx.index(msg[i:i+j]))
                i = i + j
                break
    return answer