from collections import defaultdict
import copy

def solution(record):
    answer = []
    idRecord = defaultdict(list)
    recordCopy = copy.deepcopy(record)
    for el in record:
        op = el.split(' ')
        if op[0] == 'Enter':
            idRecord[op[1]] = op[2]
        elif op[0] == 'Change':
            idRecord[op[1]] = op[2]
            
    for el in recordCopy:
        op = el.split(' ')
        if op[0] == 'Enter':
            answer.append(idRecord[op[1]] + "님이 들어왔습니다.")
        elif op[0] == 'Leave':
            answer.append(idRecord[op[1]] + "님이 나갔습니다.")
    
    return answer