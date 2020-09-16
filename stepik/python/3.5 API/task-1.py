import requests
import json

folder_path = '3.5 API/'
filename = 'dataset_24476_3.txt'

def check_number(number):
    api_url = f'http://numbersapi.com/{number}/math'
    params = {
        'json': True
    }
    res = requests.get(api_url, params=params, timeout = 25)
    data = res.json()
    if data['found']:
        return 'Interesting'
    return 'Boring'

with open(folder_path + filename, 'r') as f:
    for line in f:
        number = line.strip()
        print(check_number(number))