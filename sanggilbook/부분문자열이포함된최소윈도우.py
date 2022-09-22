import collections
S = "ADOBECODEBANC"
T = "ABC"

def minWindow(self, s: str, t: str) -> str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0
    print(need)
    # 인덱스만 +1 찾는거는 그대로
    for right, char in enumerate(s, 1):
        print('right:', right, 'char:',char, need)
        # 0보다 크면 -1 하겠다는 말
        missing -= need[char] > 0
        need[char] -= 1
        print('right:', right, need)
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not end or right - left <= end - start:
                print(right, left)
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]

minWindow('self', S,T)
