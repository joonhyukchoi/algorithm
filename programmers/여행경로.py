from collections import defaultdict, deque

def solution(tickets):
    answer = []
    dict = defaultdict(deque)
    for ticket in tickets:
        from_air, to_air = ticket[0], ticket[1]
        dict[from_air].append(to_air)
    for key in dict:
        temp = []
        temp = sorted(list(dict[key]))
        dict[key] = deque(temp)
    def dfs(start, cnt):
        try_count = len(dict[start])
        while len(dict[start]) > 0:
            try_count -= 1
            end = dict[start].popleft()
            answer.append(end)
            if dfs(end, cnt - 1):
                return True
            else:
                answer.pop()
                dict[start].append(end)
            if try_count < 0:
                return False
        if cnt > 0:
            return False
        else:
            return True
    answer.append("ICN")
    # print(dict)
    dfs('ICN', len(tickets))
    return answer