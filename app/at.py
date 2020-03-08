import requests

BASE_URL = 'https://sandboxapi.fsi.ng'
END_POINT = '/atlabs/messaging'

MAIL_URL = f'{BASE_URL}{END_POINT}'

api_key = '4295aa60c2840ff34b51b9f2a0db3ce4'

headers = {'Content-Type': "application/json", 'Sandbox-Key': api_key}


def send_message():
    data = {
            'to': '+2348130819188', 
            "from": "FSI",
            "message": "Hello World",
            "keyword": "innovation-sandbox",
            "linkId": "12345",
            "retryDurationInHours": "1"
        }
    print(requests.request("POST", MAIL_URL, json=data, headers=headers))