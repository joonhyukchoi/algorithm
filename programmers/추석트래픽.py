def solution(lines):
    times = []
    for line in lines:
        date, time, millisec = line.split(" ")
        millisec = millisec[:-1]
        millisec = int(float(millisec) * 1000)
        hour, minute, second = time.split(":")
        end_time = int(hour) * 3600 + int(minute) * 60 + float(second)
        end_time *= 1000
        start_time = end_time - millisec + 1
        times.append((start_time, end_time))
        # print(start_time, end_time)
    maxCount = 0
    for i in range(len(times)):
        count = 0
        for j in range(i, len(times)):
            if times[j][0] - 999 <= times[i][1]:
                # print(times[j], times[i])
                count += 1
        maxCount = max(maxCount, count)
    return maxCount