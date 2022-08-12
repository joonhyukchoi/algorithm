from collections import defaultdict
answer = 0
def solution(info, edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
    print(graph)
    def dfs(next_set, lamb, wolf):
        global answer
        if lamb <= wolf:
            return
        else:
            answer = max(answer, lamb)
            for next in next_set:
                child = graph[next]
                next_set |= child
                next_set -= set([next])
                if info[next] == 1:
                    wolf += 1
                else:
                    lamb += 1
                dfs(next_set, lamb, wolf)
                next_set -= child
                next_set |= set([next])
                if info[next] == 1:
                    wolf -= 1
                else:
                    lamb -= 1
                
                
    dfs(graph[0], 1, 0)
            
    return answer