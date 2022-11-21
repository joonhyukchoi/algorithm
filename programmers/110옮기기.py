from collections import deque
def solution(s):
    answer = []
    for temp_string in s:
        index = 0
        queue = deque()
        temp_arr = list(temp_string)
        temp_arr.append(3)
        temp_arr.append(3)
        temp_arr.append(3)
        for w in temp_arr:
            if temp_arr[index] == '1' \
            and temp_arr[index + 1] == '1' \
            and temp_arr[index + 2] == '1':
                if len(queue) == 0 or \
                (queue and queue[-1] <= index - 3):
                    queue.append(index)
            if temp_arr[index] == '1' \
            and temp_arr[index + 1] == '1'\
            and temp_arr[index + 2] == '0':
                if queue:
                    temp_index = queue.popleft()
                    temp_arr[index], temp_arr[index + 1], temp_arr[index + 2] \
                    = temp_arr[temp_index], temp_arr[temp_index + 1] \
                    , temp_arr[temp_index + 2]
                    temp_arr[temp_index], temp_arr[temp_index + 1] \
                    , temp_arr[temp_index + 2] = \
                    '1', '1', '0'
            index += 1
        answer.append(''.join(temp_arr[:-3]))
            
    return answer