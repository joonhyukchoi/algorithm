def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    count = 0
    for cost in costs:
        a, b, dist = cost
        if find_parent(parent, a) != find_parent(parent, b):
            answer += dist
            union(parent, a, b)
            count += 1
        if count == n - 1:
            break
    return answer