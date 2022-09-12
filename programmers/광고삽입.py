def solution(play_time, adv_time, logs):
    answer = ''
    max_time = -1
    logs_start_sec = []
    logs_end_sec = []
    play_time_sec = int(play_time[:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:])
    adv_time_sec = int(adv_time[:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:])
    logs.sort()
    for log in logs:
        log_start, logs_end = log.split('-')
        logs_start_sec.append(int(log_start[:2]) * 3600 + int(log_start[3:5]) * 60 + int(log_start[6:]))
        logs_end_sec.append(int(logs_end[:2]) * 3600 + int(logs_end[3:5]) * 60 + int(logs_end[6:]))
        
    total_time = [0] * 360001
    for i in range(0, len(logs)):
        total_time[logs_start_sec[i]] = total_time[logs_start_sec[i]] + 1
        total_time[logs_end_sec[i]] = total_time[logs_end_sec[i]] - 1
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]
    at = adv_time_sec
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= at:
            if max_time < total_time[i] - total_time[i - at]:
                answer = i - at + 1
                max_time = total_time[i] - total_time[i - at]
            # max_time = max(max_time, total_time[i] - total_time[i - at])
        else:
            if max_time < total_time[i]:
                answer = i - at + 1
                max_time = total_time[i]
            # max_time = max(max_time, total_time[i])
    answer = str(answer//3600).zfill(2)+':'+ str((answer%3600)//60).zfill(2)+':'+ str(answer%60).zfill(2)
    return answer