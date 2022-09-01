from sys import stdin
import heapq

n = int(stdin.readline()) # 건물 개수

events = []
for i in range(n):
    L, H, R = map(int, stdin.readline().split())
    events.append([L, -H, R]) # 시작지점: 건물의 왼쪽 위 끝점을 넣는다.
    events.append([R, 0, 0]) # 건물이 끝나는 지점: 오른쪽 아래 점을 따로 하나 더 저장 => 얘는 건물에 해당하지 X: 높이가 0이니.

events.sort()
print(events)

res = [[0, 0]] # 최소한 하나의 값을 출력해야 하니 더미값을 넣어준다!
live = [(0, float('inf'))] # 항상 최소로 하나의 값을 조회할 수 있어야 하기 떄문에! => 높이는 0이고 x좌표 위치는 무한대인 더미를 하나 넣어준다. 이 더미는 가장 오른쪽에 위치하겠지.


for pos, negH, R in events: # 위에서 L, -H, R이라고 저장한 애들의 이름을 각각 pos = L, negH = -H, R = R => 모든 건물에 대해 돌려본다! 가 아니라 LR 구분 없이 전부 포지션! 그러려고 위에서 [R, 0, 0]을 이벤트에 추가한 것!
    # step1: 이미 지나간 좌표값 => 제거하는 작업
    while live[0][1] <= pos: # 현재 살아있는 포지션 중에서 가장 높은 빌딩의 포지션이 지금 배치하려는 포지션의 위치보다 더 작은 곳에 있다면
        print(live[0][1], "이", pos, "보다 작아서 지나간 좌표를 제거합니다.")
        heapq.heappop(live) # live라는 heapq 데이터에서 가장 작은(여기서는 -를 붙였으니 높이가 가장 큰!)애를 뽑아온다.
    # step2. 건물을 하나씩 heap에 저장! (negH !=0: 높이가 0이 아니면 건물에 해당하니) => live에 넣어준다
    if negH:
        heapq.heappush(live, (negH, R)) # 힙에는 해당 점의 높이와 포지션(x좌표)을 넣는다. => 끝나는 지점인 R을 기준으로! 한 건물의 높이는 R에서 끝남!
         
    # step3. 마지막 높이가 highest height과 다른 경우에만 결과값에 넣어준다 (res에다가)
    if res[-1][1] != -live[0][0]: # res에는 height이 양수로 저장되어 있고 live(heap)에는 음수로 저장되어 있으니 -를 붙인다! 가장 큰 height만 활용.
        res.append(f'{pos} {-live[0][0]} ')
print("".join(res[1:]))
# 출처: https://woonys.tistory.com/entry/정글사관학교-18일차-TIL-MOO-게임5904-문자열-폭발9935-스카이라인1933 [WOONY's growth insight:티스토리]


# 이진탐색 이용한 풀이
# if not buildings:
#     return []
# height = set()
# for building in buildings:
#     L, R, H = building
#     height.add((L, -H))
#     height.add((R, H))
# ret, queue = [], [0]
# before = queue[-1]
# for P, H in sorted(height):
#     if H < 0:
#         insort(queue, -H)
#     else:
#         queue.pop(bisect_left(queue, H))
#     if queue[-1] != before:
#         ret.append([P, queue[-1]])
#         before = queue[-1]