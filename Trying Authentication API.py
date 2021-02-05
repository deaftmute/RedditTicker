import requests

API_Key = 'dd90cc834bc9030e82ac29471e3d7442'
User_agent = 'Deafmute'

headers = {
    'user-agent' : User_agent
}

payload = {
    'api_key' : API_Key,
    'method' : 'chart.gettopartists',
    'format' : 'json'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers = headers , params = payload)
print(r.status_code)

