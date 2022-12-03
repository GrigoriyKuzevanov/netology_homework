import requests

import datetime

from datetime import date, timedelta


def get_to_date():
    current_date = date.today()
    return current_date


def get_from_date():
    current_date = date.today()
    two_days = datetime.timedelta(2)
    from_date = current_date - two_days
    return from_date


def get_info():
    url = f'https://api.stackexchange.com/2.3/search'
    params = {
        'sort': 'creation', 'fromdate': get_from_date(), 'todate': get_to_date(), 'tagged': 'python', 'site': 'stackoverflow'
    }
    resp = requests.get(url, params=params)
    info = resp.json()
    for item in info['items']:
        print(f"title: {item['title']}\nid: {item['owner']['account_id']}\ndisplay name: {item['owner']['display_name']}")
        print('==============================================')


get_info()
