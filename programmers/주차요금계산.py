import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    dict = defaultdict(int)
    dictOutput = defaultdict(int)
    for record in records:
        time, car, signal = record.split()
        parseTime = list(map(int,time.split(':')))
        min = 60 * parseTime[0] + parseTime[1]
        if signal == 'IN':
            dict[car] = min
        else:
            dictOutput[car] += min - dict[car]
            dict[car] = -1
    for el in dict:
        if dict[el] != -1:
            dictOutput[el] += 60 * 23 + 59 - dict[el]
    sortedDict = sorted(dictOutput.items(), key = lambda x : x[0])
    for el in sortedDict:
        # print(fees[1],el[1], fees[0], fees[2], fees[3])
        if el[1] < fees[0]:
            answer.append(fees[1])  
        else:
            answer.append(fees[1] + math.ceil((el[1] - fees[0])/ fees[2]) * fees[3])
    return answer