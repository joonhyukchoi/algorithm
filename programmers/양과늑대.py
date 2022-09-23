# from collections import defaultdict
# answer = 0
# def solution(info, edges):
#     graph = defaultdict(set)
#     for u, v in edges:
#         graph[u].add(v)
#     print(graph)
#     def dfs(next_set, lamb, wolf):
#         global answer
#         if lamb <= wolf:
#             return
#         else:
#             answer = max(answer, lamb)
#             for next in next_set:
#                 child = graph[next]
#                 next_set |= child
#                 next_set -= set([next])
#                 if info[next] == 1:
#                     wolf += 1
#                 else:
#                     lamb += 1
#                 dfs(next_set, lamb, wolf)
#                 next_set -= child
#                 next_set |= set([next])
#                 if info[next] == 1:
#                     wolf -= 1
#                 else:
#                     lamb -= 1
                
                
#     dfs(graph[0], 1, 0)
            
#     return answer

from collections import defaultdict
import copy
answer = 0
def solution(info, edges):
    tree = defaultdict(list)
    for el in edges:
        tree[el[0]].append(el[1])
    def dfs(sons, sheep, wolf):
        global answer
        if wolf >= sheep:
            return
        else:
            answer = max(answer, sheep)
            for son in sons:
                # if tree[son]:
                new = copy.deepcopy(sons)
                for el in tree[son]:
                    new.append(el)
                new.remove(son)
                if info[son] == 1:
                    dfs(new, sheep, wolf + 1)
                else:
                    dfs(new, sheep + 1, wolf)
    dfs(tree[0], 1, 0)
    return answer
info = [0,0,1,1,1,0,1,0,1,0,1,1]	
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	
print(solution(info, edges))