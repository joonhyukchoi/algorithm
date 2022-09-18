from collections import defaultdict
def solution(user_id, banned_id):
    answer = 0
    # count_dict = defaultdict(int)
    # ban_dict = defaultdict(list)
    # for bid in banned_id:
    #     if count_dict[bid] >= 1:
    #         count_dict[bid] += 1
    #         continue
    #     for uid in user_id:
    #         if len(bid) == len(uid):
    #             count = len(bid)
    #             for i in range(len(bid)):
    #                 if bid[i] == uid[i] or bid[i] == '*':
    #                     count -= 1
    #             if count == 0:
    #                 ban_dict[bid].append(uid)
    #                 count_dict[bid] = 1
    # answer_list = []
    def check_same(uid, bid):
        if len(uid) == len(bid):
            for i in range(len(uid)):
                if uid[i] == bid[i] or bid[i] == '*':
                    pass
                else:
                    return False
        else:
            return False
        return True
    def dfs(cnt, index, id_list, answer_list):
        if cnt == len(banned_id) and id_list not in answer_list:
            temp = sorted(id_list[:])
            answer_list.append(temp)
            return
        for i in range(index, len(banned_id)):
            for uid in user_id:
                if check_same(uid, banned_id[i]) and uid not in id_list:
                    # print(uid,banned_id[i], id_list)
                    id_list.append(uid)
                    # print(id_list)
                    id_list.sort()
                    dfs(cnt + 1, i + 1, id_list, answer_list)
                    id_list.remove(uid)
    answer_list = []
    dfs(0, 0, [], answer_list)
    # print(answer_list)
    answer = len(answer_list)
    return answer