import requests

x_auth_token = '175b5568fc7b21147e6e1325785a2691'
BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'

def start_api(url, token, problem):
    url = url + '/start'
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    payload = {'problem': problem}
    response = requests.post(url, headers = headers, json = payload)
    if response.status_code == 200:
        return response.json()

def waitingLine_api(url, auth_key):
    url = url + '/waiting_line'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()

def gameResult_api(url, auth_key):
    url = url + '/game_result'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()

def userInfo_api(url, auth_key):
    url = url + '/user_info'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()

def match_api(url, auth_key, pairs):
    url = url + '/match'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    payload = {'pairs': pairs}
    response = requests.put(url, headers = headers, json = payload)
    if response.status_code == 200:
        return response.json()

def changeGrade_api(url, auth_key, commands):
    url = url + '/change_grade'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    payload = {'commands': commands}
    response = requests.put(url, headers = headers, json = payload)
    if response.status_code == 200:
        return response.json()

def score_api(url, auth_key):
    url = url + '/score'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.json()

def get_real_skill_diff(elapsed_time, D):
    return (40 - elapsed_time) * D / 35

def main_logic(BASE_URL, x_auth_token, num_users):
    start_res = start_api(BASE_URL, x_auth_token, 1)
    auth_key, problem, time = start_res['auth_key'], start_res['problem'], start_res['time']
    MIN_SKILL = 1000
    MAX_SKILL = 100000
    AVR_SKILL = 40000
    STD_SKILL = 20000
    D = MAX_SKILL - MIN_SKILL
    skills = {}
    for id in range(1, num_users + 1):
        skills[id] = AVR_SKILL
    
    for now in range(595):
        game_result_bef = gameResult_api(BASE_URL, auth_key).get('game_result', [])
        game_result = [[d['win'], d['lose'], d['taken']] for d in game_result_bef]
        for result in game_result:
            win, lose, elapsed = result
            estimate_diff = abs(skills[win] - skills[lose])
            real_diff = get_real_skill_diff(elapsed, D)
        waiting_line_bef = waitingLine_api(BASE_URL, auth_key).get('waiting_line', [])
        waiting_line = [[d['id'], now - d['from']] for d in waiting_line_bef]



if __name__ == '__main__':
    num_users = 30
    main_logic(BASE_URL, x_auth_token, num_users)
