def solution(distance, rocks, n):
    answer = 0
    # space = [0] * (len(rocks))
    rocks.append(0)
    # rocks.append(distance)
    rocks.sort()
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        dist = 0
        count = 0
        for i in range(1, len(rocks)):
            dist += rocks[i] - rocks[i - 1]
            # print('**',dist,mid)
            if dist < mid:
                count += 1
            else:
                dist = 0
        if count <= n:
            left = mid + 1
            # print(mid, count)
            answer = max(answer, mid)
        else:
            right = mid - 1
            
    return answer