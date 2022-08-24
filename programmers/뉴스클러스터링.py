from collections import defaultdict
def solution(str1, str2):
    str1Dict = defaultdict(int)
    str2Dict = defaultdict(int)
    for i in range(len(str1) - 1):
        if 'a' <= str1[i].lower() <= 'z' and 'a' <= str1[i + 1].lower() <= 'z':
            str1Dict[str1[i:i + 2].lower()] += 1
        
    for i in range(len(str2) - 1):
        if 'a' <= str2[i].lower() <= 'z' and 'a' <= str2[i + 1].lower() <= 'z':
            str2Dict[str2[i:i + 2].lower()] += 1

    count = 0
    for el in str1Dict:
        if el in str2Dict:
            count += min(str1Dict[el], str2Dict[el])
    len1 = 0
    for el in str1Dict:
        len1 += str1Dict[el]
    len2 = 0
    for el in str2Dict:
        len2 += str2Dict[el]
    if len1 + len2 - count == 0 or (len1 == 0 and len2 == 0):
        answer = 65536
    else:
        answer = count * 65536 / (len1 + len2 - count)
        answer = int(answer)
    return answer