def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp_str = ''
        temp = arr1[i] | arr2[i]
        while temp != 1:
            if temp % 2 == 1:
                temp_str += '#'
            else:
                temp_str += ' '
            temp //= 2
        temp_str += '#'
        while len(temp_str) < n:
            temp_str += ' '
        temp_str = temp_str[::-1]
        answer.append(temp_str)
        
    return answer