import requests
import json
import requests_cache
import time

requests_cache.install_cache()

API_Key = 'dd90cc834bc9030e82ac29471e3d7442'
User_agent = 'Deafmute'

def lastfm_get(payload):
    # headers and URL definition
    headers = {'user-agent': User_agent}
    url = 'http://ws.audioscrobbler.com/2.0/'

    #
    payload['api_key'] = API_Key
    payload['format'] = 'json'

    response = requests.get(url, headers= headers, params= payload)
    return response

r = lastfm_get({
    'method':'chart.gettopartists'
})

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(r.json()['artists']['@attr'])

responses = []

page = 1
total_pages = 9999

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': page
    }

    # print some output so we can see the status
    print('Requesting page {}/{}'.format(page, total_pages))
    #clear_output(wait = True)

    # make the API call
    response = lastfm_get(payload)

    # if we get an error, print the response and halt the loop
    if response.status_code != 200:
        print(response.text)
        break

    # extract pagination info
    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    # append response
    responses.append(response)

    # if it's not a cached result, sleep
    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)

    # increment the page number
    page += 1