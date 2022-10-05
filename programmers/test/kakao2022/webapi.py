import requests

x_auth_token = 'e53d8bef831cf232893238a27c208af2'
BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'

def start_api(url, token, problem):
    url = url + '/start'
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    payload = {'problem': problem}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()

def waitingLine_api(url, auth_key):
    url = url + '/waiting_line'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()

def gameResult_api(url, auth_key):
    url = url + '/game_result'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()

def userInfo_api(url, auth_key):
    url = url + '/user_info'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()

def match_api(url, auth_key, pairs):
    url = url + '/match'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    payload = {'pairs': pairs}
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()

def changeGrade_api(url, auth_key, commands):
    url = url + '/change_grade'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    payload = {'commands': commands}
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()

def score_api(url, auth_key):
    url = url + '/score'
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()

def main_logic(BASE_URL, x_auth_token):
    start_res = start_api(BASE_URL, x_auth_token, 1)
    print(start_res)
    auth_key, problem, time = start_res['auth_key'], start_res['problem'], start_res['time']
    # print('waiting', waitingLine_api(BASE_URL, auth_key))
    # print('user_info', userInfo_api(BASE_URL, auth_key))
    # print('match', match_api(BASE_URL, auth_key, []))
    # print('result', gameResult_api(BASE_URL, auth_key))
    # print('changeGrade', changeGrade_api(BASE_URL, auth_key, [{ "id": 1, "grade": 1900 }, { "id": 2, "grade": 900 }]))
    # print('match', match_api(BASE_URL, auth_key, [[1, 2], [3, 4], [5, 6]]))
    # print('waiting', waitingLine_api(BASE_URL, auth_key))
    # print('result', gameResult_api(BASE_URL, auth_key))
    # print('score', score_api(BASE_URL, auth_key))
    # print('user_info', userInfo_api(BASE_URL, auth_key))

if __name__ == '__main__':
    main_logic(BASE_URL, x_auth_token)
