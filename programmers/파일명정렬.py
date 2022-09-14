def solution(files):
    answer = []
    parsed_file = []
    for i, file in enumerate(files):
        temp_list = []
        temp_str = ''
        temp_num = ''
        for el in file:
            if el.isdigit() and len(temp_num) <= 4 and len(temp_list) <= 1:
                if temp_num == '':
                    temp_list.append(temp_str)
                    temp_str = ''
                temp_num += el
            else:
                if len(temp_num) > 0:
                    temp_list.append(temp_num)
                    temp_num = ''
                temp_str += el 
        if len(temp_num) > 0:
            temp_list.append(temp_num)
        temp_list.append(temp_str)
        temp_list.append(str(i))
        parsed_file.append(temp_list)
    parsed_file.sort(key = lambda x : (x[0].upper(), int(x[1]), int(x[3])))
    print(parsed_file)
    for file in parsed_file:
        file.pop()
        answer.append(''.join(file))
    return answer