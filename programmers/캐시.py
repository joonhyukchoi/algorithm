from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        if city.lower() not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city.lower())
            answer += 5
        else:
            cache.remove(city.lower())
            cache.append(city.lower())
            answer += 1
    return answer