from collections import deque
def solution(begin, target, words):
    answer = 0
    flag = [True] * (len(words) + 1)
    q = deque()
    q.append((begin, 0))
    while q:
        b, count = q.popleft()
        if b == target:
            answer = count
            break
        for index, word in enumerate(words):
            if len(word) == len(b):
                for i in range(len(b)):
                    temp_begin = b[:i] + b[i + 1:]
                    temp_word = word[:i] + word[i + 1:]
                    if temp_begin == temp_word and flag[index] == True:
                        flag[index] = False
                        q.append((word, count + 1))
    # def dfs(b, t, count):
    #     print(b, t, count)
    #     if b == t:
    #         return count
    #     for index, word in enumerate(words):
    #         if len(word) == len(b):
    #             for i in range(len(b)):
    #                 temp_begin = b[:i] + b[i + 1:]
    #                 temp_word = word[:i] + word[i + 1:]
    #                 print(b, word, temp_begin, temp_word)
    #                 if temp_begin == temp_word and flag[index] == True:
    #                     flag[index] = False
    #                     temp = dfs(word, t, count + 1)
    #                     if temp is not None:
    #                         return temp
    return answer