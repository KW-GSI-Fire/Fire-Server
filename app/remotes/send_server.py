import os
import requests
from dotenv import load_dotenv

# Setting - dotenv
load_dotenv()


def updateStatusToRemote(statusType, status):
    baseUrl = os.getenv('REMOTE_BASEURL')

    if statusType == 't':
        url = baseUrl + '/api/status/temperature'
    elif statusType == 'b':
        url = baseUrl + '/api/status/box'
    else:
        return

    res = requests.put(url, json=status)
    if not (res.status_code == 200):
        print('[updateStatusToRemote()] Error:', res.status_code)
